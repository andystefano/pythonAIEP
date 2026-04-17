def render_page():
    nombre = "Norbey"
    edad = 20
    activo = True

    peso = 70
    altura = 1.75
    imc = peso / (altura ** 2)

    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>NCUERVO.py</title>
      </head>
      <body style="font-family: Arial; margin: 40px;">
        <h1>Archivo NCUERVO.py</h1>
        <p>Nombre: {nombre}</p>
        <p>Edad: {edad}</p>
        <p>Curso: Python AIEP</p>
        <p>Activo: {activo}</p>
        <p>IMC: {imc:.2f}</p>
      </body>
    </html>
    """

print(render_page())   # 👈 AQUÍ VA (fuera de la función)
  