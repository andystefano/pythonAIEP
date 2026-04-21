from html import escape
from importlib import import_module

from flask import Flask, request

from ejemplos.db import get_db_connection
from ejemplos.guardar_usuario import registrar_rutas as registrar_rutas_guardar_usuario
from webhook import registrar_rutas as registrar_rutas_webhook

app = Flask(__name__)

MODULE_NAMES = [
    "AHORMAZABAL",
    "GARAVENA",
    "DOLAR",
    "DOLAR_X10",
    "INDICADORES_ECONOMICOS",
    "SELENIUM_GOOGLE",
    "JCRUZADO",
    "NCUERVO",
    "AGONZALEZ",
    "JPOBLETE",
    "SRAIN",
    "STAPIA",
    "CTRONCOSO",
    "RZAMORANO",
]

MYSQL_LINKS = [
    ("/contar-usuarios", "contar-usuarios (MySQL)"),
    ("/listar-usuarios", "listar-usuarios (MySQL)"),
    ("/formulario-usuario", "formulario-usuario (MySQL)"),
]


def render_page(title, content):
    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>{title}</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        {content}
      </body>
    </html>
    """


def render_message(title, message, back_url="/", back_label="Volver al index"):
    return render_page(
        title,
        f"""
        <h1>{title}</h1>
        <p>{message}</p>
        <a href="{back_url}">{back_label}</a>
        """,
    )


def ejecutar_update(query, params):
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute(query, params)
    conexion.commit()
    rowcount = cursor.rowcount
    cursor.close()
    conexion.close()
    return rowcount


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


@app.route("/")
def home():
    links_modulos = "".join(
        f'<li><a href="/{module_name}">{module_name}.py</a></li>'
        for module_name in MODULE_NAMES
    )
    links_mysql = "".join(
        f'<li><a href="{url}">{label}</a></li>' for url, label in MYSQL_LINKS
    )

    return render_page(
        "Rutas Python + Docker",
        f"""
        <h1>Archivo principal (index.py)</h1>
        <h2>Acceso rapido</h2>
        <ul>
          <li><a href="/DOLAR">Ver valor del dolar</a></li>
        </ul>
        <h2>Rutas de modulos</h2>
        <ul>{links_modulos}</ul>
        <h2>Rutas MySQL</h2>
        <ul>{links_mysql}</ul>
        """,
    )


@app.get("/contar-usuarios")
def contar_usuarios_url():
    from ejemplos.contar_usuarios import contar_usuarios

    total = contar_usuarios()
    return render_page(
        "Conteo de usuarios",
        f"""
        <h1>Total de usuarios: {total}</h1>
        <a href="/">Volver al index</a>
        """,
    )


@app.get("/listar-usuarios")
def listar_usuarios_url():
    from ejemplos.listar_usuarios import listar_usuarios

    usuarios = listar_usuarios()
    filas = "".join(
        (
            "<tr>"
            f"<td>{usuario['id']}</td>"
            f"<td>{escape(usuario['email'])}</td>"
            f"<td>{escape(usuario['nombre'])}</td>"
            f"<td>{escape(usuario['password'])}</td>"
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

    return render_page(
        "Listado de usuarios",
        f"""
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
        <a href="/formulario-usuario">Crear nuevo usuario</a><br />
        <a href="/">Volver al index</a>
        """,
    )


@app.get("/formulario-usuario")
def formulario_usuario_url():
    return render_page(
        "Formulario de Usuario",
        """
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
        <br />
        <a href="/listar-usuarios">Volver al listado</a><br />
        <a href="/">Volver al index</a>
        """,
    )


@app.get("/editar-usuario/<int:usuario_id>")
def editar_usuario_formulario(usuario_id):
    usuario = obtener_usuario_por_id(usuario_id)
    if not usuario:
        return (
            render_message(
                "Usuario no encontrado",
                "No existe un usuario con ese ID.",
                "/listar-usuarios",
                "Volver al listado",
            ),
            404,
        )

    email = escape(usuario["email"])
    nombre = escape(usuario["nombre"])
    password = escape(usuario["password"])

    return render_page(
        "Editar usuario",
        f"""
        <h1>Editar usuario</h1>
        <form method="post" action="/editar-usuario/{usuario['id']}">
          <label>Email:</label><br />
          <input type="email" name="email" value="{email}" required /><br /><br />

          <label>Nombre:</label><br />
          <input type="text" name="nombre" value="{nombre}" required /><br /><br />

          <label>Password:</label><br />
          <input type="text" name="password" value="{password}" required /><br /><br />

          <button type="submit">Actualizar</button>
        </form>
        <br />
        <a href="/listar-usuarios">Volver al listado</a>
        """,
    )


@app.post("/editar-usuario/<int:usuario_id>")
def editar_usuario_guardar(usuario_id):
    email = request.form.get("email", "").strip()
    nombre = request.form.get("nombre", "").strip()
    password = request.form.get("password", "").strip()

    if not email or not nombre or not password:
        return (
            render_message(
                "Faltan datos",
                "Debes completar email, nombre y password.",
                f"/editar-usuario/{usuario_id}",
                "Volver a editar",
            ),
            400,
        )

    filas_afectadas = ejecutar_update(
        "UPDATE usuarios SET email = %s, nombre = %s, password = %s WHERE id = %s",
        (email, nombre, password, usuario_id),
    )

    if filas_afectadas == 0:
        return (
            render_message(
                "Usuario no encontrado",
                "No existe un usuario con ese ID.",
                "/listar-usuarios",
                "Volver al listado",
            ),
            404,
        )

    return render_message(
        "Usuario actualizado correctamente",
        "Los datos fueron guardados en la base de datos.",
        "/listar-usuarios",
        "Volver al listado",
    )


@app.post("/eliminar-usuario/<int:usuario_id>")
def eliminar_usuario(usuario_id):
    filas_afectadas = ejecutar_update(
        "DELETE FROM usuarios WHERE id = %s",
        (usuario_id,),
    )

    if filas_afectadas == 0:
        return (
            render_message(
                "Usuario no encontrado",
                "No existe un usuario con ese ID.",
                "/listar-usuarios",
                "Volver al listado",
            ),
            404,
        )

    return render_message(
        "Usuario eliminado correctamente",
        "El registro fue eliminado de la base de datos.",
        "/listar-usuarios",
        "Volver al listado",
    )


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
registrar_rutas_webhook(app)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
