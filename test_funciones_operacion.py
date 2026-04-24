from funciones_calculo import IVA 

def test_iva_con_monto_entero():
    # ERROR: El 19% de 10000 es 1900, aquí fallará al compararlo con 2500
    assert IVA(10000) == 2500 

def test_iva_con_monto_decimal():
    # ERROR: He cambiado el decimal para que la prueba de error
    assert IVA(1234.56) == 234.00 

def test_iva_con_monto_cero():
    # ERROR: Cualquier número multiplicado por 0 es 0, aquí fallará porque espera 1
    assert IVA(0) == 1

