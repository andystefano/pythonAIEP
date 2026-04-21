# 07 - Ejercicio notas aprobadas
# Mostrar notas aprobadas (mayor o igual a 4).

notas = [3.5, 4.0, 5.5, 2.8, 6.0, 3.9]

print("Notas ingresadas:", notas)
print("Notas aprobadas:")

for nota in notas:
    if nota >= 4:
        print(nota)