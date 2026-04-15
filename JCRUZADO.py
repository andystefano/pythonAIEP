def render_page():

altura = 1.75
peso = 70 

imc = peso / (altura + altura)







    return """
    <html>
      <head>
        <meta charset="utf-8" />
        <title>JCRUZADO.py</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Archivo JCRUZADO.py</h1>
        <p>IMC: {imc:.2f}</p>
        <p>Esta ruta se esta ejecutando correctamente.</p>
        <a href="/">Volver al index</a>
      </body>
    </html>
    """
