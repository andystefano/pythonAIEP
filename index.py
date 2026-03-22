from importlib import import_module

from flask import Flask, request

from ejemplos.db import get_db_connection
from ejemplos.guardar_usuario import registrar_rutas as registrar_rutas_guardar_usuario

app = Flask(__name__)
MODULE_NAMES = [
    "AHORMAZABAL",
    "GARAVENA",
    "JCRUZADO",
    "NCUERVO",
    "AGONZALEZ",
    "JPOBLETE",
    "SRAIN",
    "STAPIA",
    "CTRONCOSO",
    "RZAMORANO",
]


@app.route("/")
def home():
    links = "".join(
        f'<li><a href="/{module_name}">{module_name}.py</a></li>'
        for module_name in MODULE_NAMES
    )
    links += '<li><a href="/contar-usuarios">contar-usuarios (MySQL)</a></li>'
    links += '<li><a href="/listar-usuarios">listar-usuarios (MySQL)</a></li>'
    links += '<li><a href="/formulario-usuario">formulario-usuario (MySQL)</a></li>'
    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>Rutas Python + Docker</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Archivo principal (index.py)</h1>
        <p>Selecciona una ruta para abrir su archivo finallu:</p>
        <ul>
          {links}
        </ul>
      </body>
    </html>
    """


@app.get("/contar-usuarios")
def contar_usuarios_url():
    from ejemplos.contar_usuarios import contar_usuarios

    total = contar_usuarios()
    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>Conteo de usuarios</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Total de usuarios: {total}</h1>
        <a href="/">Volver al index</a>
      </body>
    </html>
    """


@app.get("/listar-usuarios")
def listar_usuarios_url():
    from ejemplos.listar_usuarios import listar_usuarios

    usuarios = listar_usuarios()
    filas = "".join(
        (
            "<tr>"
            f"<td>{usuario['id']}</td>"
            f"<td>{usuario['email']}</td>"
            f"<td>{usuario['nombre']}</td>"
            f"<td>{usuario['password']}</td>"
            "<td>"
            f'<a href="/editar-usuario/{usuario["id"]}">Editar</a> '
            '<form method="post" '
            f'action="/eliminar-usuario/{usuario["id"]}" '
            'style="display:inline;" '
            'onsubmit="return confirm(\'¿Seguro que deseas eliminar este usuario?\');">'
            '<button type="submit">Eliminar</button>'
            "</form>"
            "</td>"
            "</tr>"
        )
        for usuario in usuarios
    )

    if not filas:
        filas = (
            '<tr><td colspan="5" style="text-align:center;">'
            "No hay usuarios registrados."
            "</td></tr>"
        )

    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>Listado de usuarios</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Listado de usuarios</h1>
        <table border="1" cellpadding="8" cellspacing="0">
          <thead>
            <tr>
              <th>ID</th>
              <th>Email</th>
              <th>Nombre</th>
              <th>Password</th>
              <th>Acciones</th>
            </tr>
          </thead>
          <tbody>
            {filas}
          </tbody>
        </table>
        <br />
        <a href="/">Volver al index</a>
      </body>
    </html>
    """


def obtener_usuario_por_id(usuario_id):
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute(
        "SELECT id, email, nombre, password FROM usuarios WHERE id = %s",
        (usuario_id,),
    )
    usuario = cursor.fetchone()
    cursor.close()
    conexion.close()
    return usuario


@app.get("/editar-usuario/<int:usuario_id>")
def editar_usuario_formulario(usuario_id):
    usuario = obtener_usuario_por_id(usuario_id)
    if not usuario:
        return """
        <h2>Usuario no encontrado</h2>
        <a href="/listar-usuarios">Volver al listado</a>
        """, 404

    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>Editar usuario</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Editar usuario</h1>
        <form method="post" action="/editar-usuario/{usuario['id']}">
          <label>Email:</label><br />
          <input type="email" name="email" value="{usuario['email']}" required /><br /><br />

          <label>Nombre:</label><br />
          <input type="text" name="nombre" value="{usuario['nombre']}" required /><br /><br />

          <label>Password:</label><br />
          <input type="text" name="password" value="{usuario['password']}" required /><br /><br />

          <button type="submit">Actualizar</button>
        </form>
        <br />
        <a href="/listar-usuarios">Volver al listado</a>
      </body>
    </html>
    """


@app.post("/editar-usuario/<int:usuario_id>")
def editar_usuario_guardar(usuario_id):
    email = request.form.get("email", "").strip()
    nombre = request.form.get("nombre", "").strip()
    password = request.form.get("password", "").strip()

    if not email or not nombre or not password:
        return """
        <h2>Faltan datos</h2>
        <p>Debes completar email, nombre y password.</p>
        <a href="/listar-usuarios">Volver al listado</a>
        """, 400

    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute(
        "UPDATE usuarios SET email = %s, nombre = %s, password = %s WHERE id = %s",
        (email, nombre, password, usuario_id),
    )
    conexion.commit()
    filas_afectadas = cursor.rowcount
    cursor.close()
    conexion.close()

    if filas_afectadas == 0:
        return """
        <h2>Usuario no encontrado</h2>
        <a href="/listar-usuarios">Volver al listado</a>
        """, 404

    return """
    <h2>Usuario actualizado correctamente</h2>
    <a href="/listar-usuarios">Volver al listado</a>
    """


@app.post("/eliminar-usuario/<int:usuario_id>")
def eliminar_usuario(usuario_id):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id = %s", (usuario_id,))
    conexion.commit()
    filas_afectadas = cursor.rowcount
    cursor.close()
    conexion.close()

    if filas_afectadas == 0:
        return """
        <h2>Usuario no encontrado</h2>
        <a href="/listar-usuarios">Volver al listado</a>
        """, 404

    return """
    <h2>Usuario eliminado correctamente</h2>
    <a href="/listar-usuarios">Volver al listado</a>
    """


@app.get("/formulario-usuario")
def formulario_usuario_url():
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


def build_module_route(module_name):
    def route_handler():
        module = import_module(module_name)
        return module.render_page()

    route_handler.__name__ = f"route_{module_name.lower()}"
    return route_handler


for module_name in MODULE_NAMES:
    app.add_url_rule(
        f"/{module_name}",
        endpoint=module_name,
        view_func=build_module_route(module_name),
    )

registrar_rutas_guardar_usuario(app)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
