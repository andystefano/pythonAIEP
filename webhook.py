import os
import requests
from flask import request, jsonify

MAILGUN_API_KEY = os.getenv("mailgun_api_key", "")
MAILGUN_DOMAIN = "sandbox63cc9589838a4c69918c906ea969ece5.mailgun.org"


def enviar_email(destinatario, number):
    return requests.post(
        f"https://api.mailgun.net/v3/{MAILGUN_DOMAIN}/messages",
        auth=("api", MAILGUN_API_KEY),
        data={
            "from": f"Liquidaciones <postmaster@{MAILGUN_DOMAIN}>",
            "to": destinatario,
            "subject": "Solicitud de liquidaciones de sueldo",
            "text": (
                f"Se han solicitado {number} liquidaciones de sueldo. "
                "Serán enviadas a la brevedad."
            ),
        },
    )


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

            enviar_email(email, number)

            return jsonify({
                "fulfillmentText": (
                    f"Pidió {number} liquidaciones, "
                    f"a través de backend al email {email} "
                    "... que serán enviadas"
                )
            })

        return jsonify({
            "fulfillmentText": "No entendí la solicitud"
        })
