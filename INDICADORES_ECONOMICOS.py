from html import escape

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

URL_BCENTRAL = "https://www.bcentral.cl/inicio"

SELECTORES_INDICADORES = {
    "UF": "#_BcentralIndicadoresViewer_INSTANCE_pLcePZ0Eybi8_myTooltipDelegate > div > div > div.fin-indicators-col1 > div > div > div:nth-child(1) > div > p.basic-text.fs-2.f-opensans-bold.text-center.c-blue-nb-2",
    "UTM (ABR)": "#_BcentralIndicadoresViewer_INSTANCE_pLcePZ0Eybi8_myTooltipDelegate > div > div > div.fin-indicators-col1 > div > div > div:nth-child(2) > div > p.basic-text.fs-2.f-opensans-bold.text-center.c-blue-nb-2",
    # BEC no venia en tu lista de selectores, se asume que es el bloque 3.
    "BEC": "#_BcentralIndicadoresViewer_INSTANCE_pLcePZ0Eybi8_myTooltipDelegate > div > div > div.fin-indicators-col1 > div > div > div:nth-child(3) > div > p.basic-text.fs-2.f-opensans-bold.text-center.c-blue-nb-2",
    "Dólar Observado": "#_BcentralIndicadoresViewer_INSTANCE_pLcePZ0Eybi8_myTooltipDelegate > div > div > div.fin-indicators-col1 > div > div > div:nth-child(4) > div > p.basic-text.fs-2.f-opensans-bold.text-center.c-blue-nb-2",
    "Dólar en línea": "#_BcentralIndicadoresViewer_INSTANCE_pLcePZ0Eybi8_myTooltipDelegate > div > div > div.fin-indicators-col1 > div > div > div:nth-child(5) > div > p.basic-text.fs-2.f-opensans-bold.text-center.c-blue-nb-2",
    "Euro": "#_BcentralIndicadoresViewer_INSTANCE_pLcePZ0Eybi8_myTooltipDelegate > div > div > div.fin-indicators-col1 > div > div > div:nth-child(6) > div > p.basic-text.fs-2.f-opensans-bold.text-center.c-blue-nb-2",
}


def obtener_texto_por_selector(driver, wait, selector):
    elemento = wait.until(ec.visibility_of_element_located((By.CSS_SELECTOR, selector)))
    texto = elemento.text.strip()
    return texto or "No encontrado"


def obtener_indicadores():
    driver = webdriver.Chrome()  # o webdriver.Firefox()
    try:
        driver.get(URL_BCENTRAL)
        wait = WebDriverWait(driver, 20)
        indicadores = {}
        for nombre, selector in SELECTORES_INDICADORES.items():
            try:
                indicadores[nombre] = obtener_texto_por_selector(driver, wait, selector)
            except Exception:
                indicadores[nombre] = "No encontrado"

        return indicadores
    finally:
        driver.quit()


def render_page():
    try:
        indicadores = obtener_indicadores()
        filas = "".join(
            f"<tr><td>{escape(nombre)}</td><td>{escape(valor)}</td></tr>"
            for nombre, valor in indicadores.items()
        )
        contenido = f"""
        <h1>Indicadores Economicos</h1>
        <p>Fuente: <a href="{URL_BCENTRAL}" target="_blank">Banco Central de Chile</a></p>
        <table border="1" cellpadding="8" cellspacing="0">
          <thead>
            <tr>
              <th>Indicador</th>
              <th>Valor</th>
            </tr>
          </thead>
          <tbody>
            {filas}
          </tbody>
        </table>
        <br />
        <a href="/">Volver al index</a>
        """
    except Exception as error:
        contenido = f"""
        <h1>Indicadores Economicos</h1>
        <p>No fue posible obtener los indicadores desde el sitio.</p>
        <p>Detalle: {escape(str(error))}</p>
        <a href="/">Volver al index</a>
        """

    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>INDICADORES_ECONOMICOS.py</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        {contenido}
      </body>
    </html>
    """
