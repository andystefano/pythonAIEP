from funciones_calculo import IVA

def test_iva_con_monto_entero():
    assert IVA(10000) == 1900

def test_iva_con_monto_decimal():
    assert IVA(1234.56) == 234.5664

def test_iva_con_monto_cero():
    # El profe aquí puso == 1 para mostrar un error, 
    # pero lo correcto es 0
    assert IVA(0) == 1