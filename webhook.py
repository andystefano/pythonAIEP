from flask import request, jsonify

from ejemplos.db import get_db_connection


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

        return jsonify({
            "fulfillmentText": "No entendí la solicitud"
        })
