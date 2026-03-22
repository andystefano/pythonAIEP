from flask import Flask

try:
    from ejemplos.guardar_usuario import registrar_rutas as registrar_ruta_guardado
except ModuleNotFoundError:
    from guardar_usuario import registrar_rutas as registrar_ruta_guardado

app = Flask(__name__)


@app.get("/formulario-usuario")
def formulario_usuario():
    return """
    <html>
      <head>
        <meta charset="utf-8" />
        <title>Formulario de Usuario</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Registrar usuario</h1>
        <form method="post" action="/guardar-usuario">
          <label>Email:</label><br />
          <input type="email" name="email" required /><br /><br />

          <label>Nombre:</label><br />
          <input type="text" name="nombre" required /><br /><br />

          <label>Password:</label><br />
          <input type="text" name="password" required /><br /><br />

          <button type="submit">Guardar</button>
        </form>
      </body>
    </html>
    """


registrar_ruta_guardado(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)
