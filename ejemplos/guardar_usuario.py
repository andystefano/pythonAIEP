from flask import request

from db import get_db_connection


def registrar_rutas(app):
    @app.post("/guardar-usuario")
    def guardar_usuario():
        email = request.form.get("email", "").strip()
        nombre = request.form.get("nombre", "").strip()
        password = request.form.get("password", "").strip()

        if not email or not nombre or not password:
            return """
            <h2>Faltan datos</h2>
            <p>Debes completar email, nombre y password.</p>
            <a href="/formulario-usuario">Volver al formulario</a>
            """, 400

        conexion = None
        cursor = None
        try:
            conexion = get_db_connection()
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO usuarios (email, nombre, password) VALUES (%s, %s, %s)",
                (email, nombre, password),
            )
            conexion.commit()
        except Exception as error:
            return f"""
            <h2>Error al guardar</h2>
            <p>{error}</p>
            <a href="/formulario-usuario">Volver al formulario</a>
            """, 500
        finally:
            if cursor:
                cursor.close()
            if conexion:
                conexion.close()

        return f"""
        <h2>Usuario guardado correctamente</h2>
        <p>Nombre: {nombre}</p>
        <p>Email: {email}</p>
        <a href="/formulario-usuario">Ingresar otro usuario</a>
        """
