from flask import request, jsonify


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

        return jsonify({
            "fulfillmentText": "No entendí la solicitud"
        })
