nombre = "Andy"
numero1 = 6
numero2 = 7
resultado = numero1 * numero2


def render_page():
    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>AHORMAZABAL.py</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Archivo AHORMAZABAL.py</h1>
        <p>Esta ruta se esta ejecutando correctamente.</p>
        <p>Nombre: {nombre}</p>
        <p>Resultado (numero1 * numero2): {resultado}</p>
        <a href="/">Volver al index</a>
      </body>
    </html>
    """
