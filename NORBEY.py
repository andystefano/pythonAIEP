def render_page():
    # --- Lógica del IMC ---
    nombre = "Norbey"
    peso = 70  # Puedes cambiar este número
    estatura = 1.70 # Puedes cambiar este número
    
    # Fórmula: peso / (estatura * estatura)
    imc = peso / (estatura ** 2)
    imc_redondeado = round(imc, 2)

    # --- El diseño ---
    return f"""
    <html>
      <body style="background-color: #0d1117; color: white; font-family: 'Segoe UI', sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0;">
        <div style="background-color: #161b22; padding: 40px; border-radius: 20px; border: 2px solid #58a6ff; text-align: center; box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
            <h1 style="color: #58a6ff;">📊 Calculadora de IMC</h1>
            <h2 style="margin-bottom: 5px;">Usuario: {nombre}</h2>
            <hr style="border: 0; border-top: 1px solid #30363d; margin: 20px 0;">
            
            <p style="font-size: 1.2em;">Peso: {peso}kg | Estatura: {estatura}m</p>
            
            <div style="background: #21262d; padding: 15px; border-radius: 10px; margin: 20px 0;">
                <h3 style="margin: 0; color: #3fb950;">Tu IMC es: {imc_redondeado}</h3>
            </div>

            <p style="color: #8b949e; font-size: 0.9em;">Esta ruta se está ejecutando correctamente desde NORBEY.py</p>
            
            <br>
            <a href="/" style="text-decoration: none; color: #58a6ff; font-weight: bold; border: 1px solid #58a6ff; padding: 10px 20px; border-radius: 5px;">
                Volver al index
            </a>
        </div>
      </body>
    </html>
    """