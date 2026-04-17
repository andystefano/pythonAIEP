nombre = "Andy"
numero1 = 5
numero2 = 3
resultado = numero1 * numero2
notas = [5.5, 4.0, 6.2, 3.8, 4.7]
promedio = sum(notas) / len(notas)
color_promedio = "green" if promedio >= 4 else "red"


def render_page():
    filas_notas = "".join(
        f"<tr><td>{indice}</td><td>{nota:.1f}</td></tr>"
        for indice, nota in enumerate(notas, start=1)
    )

    return f"""
    <html>
      <head>
        <meta charset="utf-8" />
        <title>AHORMAZABAL.py</title>
      </head>
      <body style="font-family: Arial, sans-serif; margin: 40px;">
        <h1>Archivo AHORMAZABAL.py</h1>
        <p>Esta ruta se esta ejecutando correctamente.</p>
        <p>Nombre: {nombre}</p>
        <p>Resultado (numero1 * numero2): {resultado}</p>
        <h2>Notas</h2>
        <table border="1" cellpadding="8" cellspacing="0">
          <thead>
            <tr>
              <th>N°</th>
              <th>Nota</th>
            </tr>
          </thead>
          <tbody>
            {filas_notas}
          </tbody>
        </table>
        <p>
          Promedio:
          <strong style="color: {color_promedio};">{promedio:.1f}</strong>
        </p>
        <a href="/">Volver al index</a>
      </body>
    </html>
    """
