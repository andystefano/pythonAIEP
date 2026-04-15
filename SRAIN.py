def render_page():
    altura = 1.65      # Numero decimal (float)
    peso = 70          # Peso en kg
    imc = peso / (altura ** 2)  # Calcula el indice de masa corporal

    return """
    <html>
      <head>
        <meta charset="utf-8" />
        <title>ZRAIN.py</title>
        <p>> IMC: {imc}</p>

      </head>
      <body style="font-family: Arial, sans-serif; margin: 70px;">
        <h1>Archivo SRAIN.py</h1>
        <p>Esta ruta se esta ejecutando correctamente.</p>
        <a href="/">Volver al index</a>
      </body>
    </html>
    """
