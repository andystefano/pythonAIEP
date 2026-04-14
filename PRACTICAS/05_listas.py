# 05 - Listas
# Una lista guarda varios datos en orden.

nombres = ["Ana", "Luis", "Marta", "Pedro"]

print("Lista completa:", nombres)
print("Primer nombre:", nombres[0])

# Recorrer la lista con for.
for nombre in nombres:
    print("Hola", nombre)

# Agregar un nuevo elemento.
nombres.append("Sofia")
print("Lista actualizada:", nombres)
