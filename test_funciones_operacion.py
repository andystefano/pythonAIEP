from funciones_calculo import IVA

### --- PRUEBAS UNITARIAS PARA IVA ---

def test_iva_con_monto_entero():
    """Prueba que el 19% de un número entero se calcule correctamente"""
    monto = 10000
    esperado = 1900
    print(f"Probando IVA de {monto}: debe ser {esperado}")
    assert IVA(monto) == esperado

def test_iva_con_monto_decimal():
    """Prueba el cálculo con números decimales (precisión)"""
    monto = 1234.56
    esperado = 234.5664
    assert IVA(monto) == esperado

def test_iva_con_monto_cero():
    """Prueba el comportamiento con valor cero"""
    assert IVA(0) == 0

### --- PRUEBAS ADICIONALES (Basadas en tu proyecto) ---

def test_iva_monto_negativo():
    """Opcional: Verifica cómo se comporta con números negativos"""
    assert IVA(-100) == -19

# Si tienes la función IMC en funciones_calculo, puedes agregar:
# from funciones_calculo import calcular_imc
# def test_imc_normal():
#     assert calcular_imc(70, 1.75) == 22.86