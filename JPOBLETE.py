altura = 1.73
peso = 95

imc = peso / (altura * altura)

def render_page():

    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>JPOBLETE.py</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Archivo JPOBLETE.py</h1>
        <p>IMC: {imc:.2f}</p>
        <p>Esta ruta se esta ejecutando correctamente.</p>
        <a href="/">Volver al index</a>
      </body>
    </html>
    """
