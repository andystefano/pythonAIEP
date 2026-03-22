from importlib import import_module

from flask import Flask

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


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
