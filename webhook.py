import os

from flask import request, jsonify
from openai import OpenAI

from ejemplos.db import get_db_connection, get_env_config


def _openai_api_key():
    return (os.environ.get("openai") or get_env_config().get("openai") or "").strip()


def _significado_del_nombre(nombre):
    api_key = _openai_api_key()
    if not api_key:
        raise ValueError("Falta la clave de API OpenAI (variable openai).")

    client = OpenAI(api_key=api_key)
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": (
                    f"Explica de forma breve y clara en español cuál es el significado "
                    f"y el origen (etimología o cultura) del nombre propio: «{nombre}». "
                    "Si es ambiguo, menciona las variantes más comunes."
                ),
            }
        ],
        max_tokens=500,
    )
    return (completion.choices[0].message.content or "").strip()


def _guardar_concursante(nombre, apellido, email, telefono):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute(
        "INSERT INTO concursantes (nombre, apellido, email, telefono) VALUES (%s, %s, %s, %s)",
        (nombre, apellido, email, telefono),
    )
    conexion.commit()
    cursor.close()
    conexion.close()


def registrar_rutas(app):
    @app.post("/webhook")
    def webhook():
        data = request.get_json(silent=True) or {}

        intent = (
            data.get("queryResult", {})
                .get("intent", {})
                .get("displayName", "")
        )

        if intent == "SolicitudLiquidacionSueldo":
            params = data.get("queryResult", {}).get("parameters", {})
            number = params.get("number", 0)
            email = params.get("email", "")

            return jsonify({
                "fulfillmentText": (
                    f"Pidió {number} liquidaciones, "
                    f"a través de backend al email {email} "
                    "... que serán enviadas"
                )
            })

        if intent == "SolicitudRegistroConcursante":
            params = data.get("queryResult", {}).get("parameters", {})
            nombre = params.get("nombre", "").strip()
            apellido = params.get("apellido", "").strip()
            email = params.get("email", "").strip()
            telefono = params.get("telefono", "").strip()

            if not nombre or not apellido or not email:
                return jsonify({
                    "fulfillmentText": "Faltan datos obligatorios: nombre, apellido y email son requeridos."
                })

            try:
                _guardar_concursante(nombre, apellido, email, telefono)
                return jsonify({
                    "fulfillmentText": (
                        f"Concursante {nombre} {apellido} registrado correctamente "
                        f"con el email {email}."
                    )
                })
            except Exception as e:
                return jsonify({
                    "fulfillmentText": f"Error al registrar el concursante: {str(e)}"
                })

        if intent == "significadoNombre":
            params = data.get("queryResult", {}).get("parameters", {})
            nombre = (params.get("nombre") or "").strip()

            if not nombre:
                return jsonify({
                    "fulfillmentText": "Indica un nombre para consultar su significado y origen."
                })

            try:
                texto = _significado_del_nombre(nombre)
                return jsonify({"fulfillmentText": texto})
            except ValueError as e:
                return jsonify({"fulfillmentText": str(e)})
            except Exception as e:
                return jsonify({
                    "fulfillmentText": f"No pude consultar el significado del nombre: {str(e)}"
                })

        return jsonify({
            "fulfillmentText": "No entendí la solicitud"
        })
