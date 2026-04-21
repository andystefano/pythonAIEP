from html import escape

from selenium import webdriver


def obtener_titulo_google():
    driver = webdriver.Chrome()  # o webdriver.Firefox()
    try:
        driver.get("https://www.google.com")
        return driver.title
    finally:
        driver.quit()


def render_page():
    try:
        titulo = obtener_titulo_google()
        mensaje = f"Titulo obtenido con Selenium: {escape(titulo)}"
    except Exception as error:
        mensaje = (
            "No se pudo abrir Selenium en este entorno. "
            f"Detalle: {escape(str(error))}"
        )

    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>SELENIUM_GOOGLE.py</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Vista SELENIUM_GOOGLE.py</h1>
        <p>{mensaje}</p>
        <a href="/">Volver al index</a>
      </body>
    </html>
    """


if __name__ == "__main__":
    print(obtener_titulo_google())
