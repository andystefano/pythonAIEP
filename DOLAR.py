from html import escape

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

URL_BCENTRAL = "https://www.bcentral.cl/inicio"

SELECTOR_DOLAR_OBSERVADO = (
    "#_BcentralIndicadoresViewer_INSTANCE_pLcePZ0Eybi8_myTooltipDelegate > div > div > "
    "div.fin-indicators-col1 > div > div > div:nth-child(4) > div > "
    "p.basic-text.fs-2.f-opensans-bold.text-center.c-blue-nb-2"
)


def obtener_valor_dolar():
    driver = webdriver.Chrome()  # o webdriver.Firefox()
    try:
        driver.get(URL_BCENTRAL)
        wait = WebDriverWait(driver, 20)
        elemento = wait.until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, SELECTOR_DOLAR_OBSERVADO))
        )
        texto = elemento.text.strip()
        return texto or "No encontrado"
    finally:
        driver.quit()


def render_page():
    try:
        valor_dolar = obtener_valor_dolar()
        contenido = f"""
        <h1>Valor del Dolar</h1>
        <p>Fuente: <a href="{URL_BCENTRAL}" target="_blank">Banco Central de Chile</a></p>
        <p><strong>Dolar Observado:</strong> {escape(valor_dolar)}</p>
        <a href="/">Volver al index</a>
        """
    except Exception as error:
        contenido = f"""
        <h1>Valor del Dolar</h1>
        <p>No fue posible obtener el valor del dolar.</p>
        <p>Detalle: {escape(str(error))}</p>
        <a href="/">Volver al index</a>
        """

    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>DOLAR.py</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        {contenido}
      </body>
    </html>
    """
