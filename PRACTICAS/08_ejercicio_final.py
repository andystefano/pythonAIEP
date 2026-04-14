# 08 - Ejercicio final
# Combina variables, listas, if y for.

curso = "Python basico"
alumnos = ["Ana", "Luis", "Marta", "Pedro"]
notas = [5.0, 3.8, 6.2, 4.1]

print("Curso:", curso)
print("Resultado final:")

for i in range(len(alumnos)):
    alumno = alumnos[i]
    nota = notas[i]

    if nota >= 4:
        estado = "Aprobado"
    else:
        estado = "Reprobado"

    print(alumno, "- Nota:", nota, "-", estado)
