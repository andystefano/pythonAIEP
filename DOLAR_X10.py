import re
from html import escape

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

from funciones_calculo import IVA

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


def parsear_monto(texto):
    limpio = re.sub(r"[^0-9,.-]", "", texto)
    if "," in limpio and "." in limpio:
        limpio = limpio.replace(".", "").replace(",", ".")
    elif "," in limpio:
        limpio = limpio.replace(",", ".")
    return float(limpio)


def render_page():
    try:
        valor_dolar_texto = obtener_valor_dolar()
        valor_dolar = parsear_monto(valor_dolar_texto)
        total_10_dolares = valor_dolar * 10
        iva_10_dolares = IVA(total_10_dolares)

        contenido = f"""
        <h1>Valor del Dolar + Calculo de 10 USD</h1>
        <p>Fuente: <a href="{URL_BCENTRAL}" target="_blank">Banco Central de Chile</a></p>
        <p><strong>Dolar Observado:</strong> {escape(valor_dolar_texto)}</p>
        <p><strong>10 dolares equivalen a:</strong> ${total_10_dolares:,.2f} CLP</p>
        <p><strong>IVA (19%) sobre ese monto:</strong> ${iva_10_dolares:,.2f} CLP</p>
        <a href="/">Volver al index</a>
        """
    except Exception as error:
        contenido = f"""
        <h1>Valor del Dolar + Calculo de 10 USD</h1>
        <p>No fue posible obtener el valor del dolar o calcular 10 USD.</p>
        <p>Detalle: {escape(str(error))}</p>
        <a href="/">Volver al index</a>
        """

    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>DOLAR_X10.py</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        {contenido}
      </body>
    </html>
    """
