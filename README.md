# Guia basica de Python (paso a paso)

Este documento explica, de forma simple, los conceptos base de Python :

- Variables
- Constantes
- Arreglos (listas)
- Funciones
- If
- "Switch" (en Python se usa `match`)
- Estructuras de control
- Operadores (asignacion, comparacion, logicos, etc.)

---

## 1) Variables

Una variable guarda un valor para usarlo despues.

```python
nombre = "Andy"
edad = 25
activo = True
```

### Paso a paso
1. Escribes un nombre de variable (`nombre`).
2. Usas `=` para asignar un valor.
3. Python detecta el tipo automaticamente (`str`, `int`, `bool`, etc.).

---

## 2) Constantes

Python no tiene constantes "reales", pero por convencion se escriben en MAYUSCULA.

```python
PI = 3.1416
URL_API = "https://api.ejemplo.com"
```

> Regla de equipo: si esta en mayuscula, no deberia cambiar.

---

## 3) Arreglos (Listas)

En Python normalmente hablamos de **listas**.

```python
nombres = ["Ana", "Luis", "Pedro"]
```

### Operaciones comunes

```python
print(nombres[0])        # Ana
nombres.append("Maria")  # agrega al final
nombres[1] = "Luisa"     # modifica posicion 1
print(len(nombres))      # cantidad de elementos
```

---

## 4) Funciones

Una funcion agrupa codigo reutilizable.

```python
def saludar(nombre):
    return f"Hola, {nombre}"
```

### Paso a paso
1. `def` inicia la funcion.
2. `saludar` es el nombre.
3. `(nombre)` es el parametro de entrada.
4. `return` devuelve un resultado.

Uso:

```python
mensaje = saludar("Andy")
print(mensaje)  # Hola, Andy
```

---

## 5) If (condicionales)

`if` permite tomar decisiones.

```python
edad = 20

if edad >= 18:
    print("Es mayor de edad")
else:
    print("Es menor de edad")
```

Con multiples condiciones:

```python
nota = 5.5

if nota >= 6:
    print("Excelente")
elif nota >= 4:
    print("Aprobado")
else:
    print("Reprobado")
```

---

## 6) Switch en Python (`match-case`)

En Python moderno (3.10+) se usa `match`.

```python
dia = 3

match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case 3:
        print("Miercoles")
    case _:
        print("Dia no valido")
```

`case _` funciona como `default`.

---

## 7) Estructuras de control

### 7.1 Bucle `for`

```python
for i in range(1, 4):
    print(i)
```

Salida: `1`, `2`, `3`

### 7.2 Bucle `while`

```python
contador = 1
while contador <= 3:
    print(contador)
    contador += 1
```

### 7.3 `break`, `continue`, `pass`

```python
for n in range(1, 6):
    if n == 2:
        continue  # salta esta vuelta
    if n == 5:
        break     # corta el bucle
    print(n)
```

`pass` se usa cuando quieres dejar un bloque "vacio" temporalmente.

---

## 8) Operadores

## 8.1 Asignacion

```python
x = 10
x += 5   # x = x + 5
x -= 2
x *= 3
x /= 2
```

## 8.2 Comparacion

```python
a = 10
b = 20

print(a == b)  # igual

Hablar de la diferencia entre igual he identico
print(a != b)  # distinto
print(a > b)   # mayor
print(a < b)   # menor
print(a >= b)  # mayor o igual
print(a <= b)  # menor o igual
```

## 8.3 Logicos

```python
usuario_activo = True
tiene_permiso = False

print(usuario_activo and tiene_permiso)  # True si ambos son True
print(usuario_activo or tiene_permiso)   # True si al menos uno es True
print(not usuario_activo)                # invierte True/False
```

## 8.4 Aritmeticos

```python
print(10 + 2)   # suma
print(10 - 2)   # resta
print(10 * 2)   # multiplicacion
print(10 / 2)   # division
print(10 // 3)  # division entera
print(10 % 3)   # modulo (resto)
print(2 ** 3)   # potencia
```

---

## 9) Ejemplo completo corto

```python
EDAD_MINIMA = 18
usuarios = [
    {"nombre": "Ana", "edad": 17},
    {"nombre": "Luis", "edad": 22},
]

def puede_entrar(edad):
    return edad >= EDAD_MINIMA

for usuario in usuarios:
    nombre = usuario["nombre"]
    edad = usuario["edad"]

    if puede_entrar(edad):
        estado = "Puede entrar"
    else:
        estado = "No puede entrar"

    print(f"{nombre}: {estado}")
```

---

## 10) Recomendaciones practicas

1. Usa nombres claros: `total_usuarios`, `email_cliente`.
2. Evita "numeros magicos"; usa constantes.
3. Divide problemas en funciones pequenas.
4. Valida datos con `if` antes de procesar.
5. Comenta solo lo necesario y manten el codigo simple.

