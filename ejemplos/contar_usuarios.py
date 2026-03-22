from db import get_db_connection


def contar_usuarios():
    conexion = get_db_connection()
    cursor = conexion.cursor()
    cursor.execute("SELECT COUNT(*) FROM usuarios")
    total = cursor.fetchone()[0]
    cursor.close()
    conexion.close()
    return total


if __name__ == "__main__":
    print(f"Total de usuarios: {contar_usuarios()}")
