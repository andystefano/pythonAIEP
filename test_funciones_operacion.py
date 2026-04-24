<<<<<<< HEAD
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

=======
from funciones_calculo import IVA

def test_iva_con_monto_entero():
    assert IVA(10000) == 1900

def test_iva_con_monto_decimal():
    assert IVA(1234.56) == 234.5664

def test_iva_con_monto_cero():
    # El profe aquí puso == 1 para mostrar un error, 
    # pero lo correcto es 0
    assert IVA(0) == 0
>>>>>>> 262b5ffcec2b4ca0616c1d8bcb8bf34b1f2ad6dd
