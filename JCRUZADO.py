altura = 1.65      # Numero decimal (float)
peso = 70          # Numero entero (int)

imc = peso / (altura * altura)


def render_page():
    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>JCRUZADO.py</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">

        <h1>Archivo JCRUZADO.py</h1>
        <p>IMC: {imc:.2f} *****</p>
        <p>Esta ruta se esta ejecutando correctamente.</p>
        <a href="/">Volver al index</a>
      </body>
    </html>
    f"""
