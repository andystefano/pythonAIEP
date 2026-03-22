from db import get_db_connection


def listar_usuarios():
    conexion = get_db_connection()
    cursor = conexion.cursor(dictionary=True)
    cursor.execute("SELECT id, email, nombre, password FROM usuarios ORDER BY id")
    usuarios = cursor.fetchall()
    cursor.close()
    conexion.close()
    return usuarios


if __name__ == "__main__":
    usuarios = listar_usuarios()
    if not usuarios:
        print("No hay usuarios en la tabla usuarios.")
    else:
        for usuario in usuarios:
            print(
                f"id={usuario['id']} | email={usuario['email']} | "
                f"nombre={usuario['nombre']} | password={usuario['password']}"
            )
