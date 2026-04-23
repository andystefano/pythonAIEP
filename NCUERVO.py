def render_page():
    # DATOS
    nombre = "NORBEY"
    peso = 70
    estatura = 1.70
    
    # CÁLCULO
    imc = peso / (estatura * estatura)
    imc_redondeado = round(imc, 2)

    # HTML PURO (SIN ESTILOS)
    return f"""
    <html>
      <body>
        <p>> IMC: {imc_redondeado}</p>
        <h1>Archivo {nombre}.py</h1>
        <p>Esta ruta se esta ejecutando correctamente.</p>
        <br>
        <a href="/">Volver al index</a>
      </body>
    </html>
    """