# Clasificador de datos
# Dada una lista de calificaciones, clasifica cada una y cuenta los resultados

calificaciones = [9.5, 7.2, 5.8, 8.0, 6.5, 9.0, 4.3, 7.8, 10.0, 3.5]

excelentes = 0
buenos = 0
suficientes = 0
reprobados = 0

for calif in calificaciones:
    if calif >= 9:
        excelentes += 1
        categoria = "Excelente"
    elif calif >= 7:
        buenos += 1
        categoria = "Bueno"
    elif calif >= 6:
        suficientes += 1
        categoria = "Suficiente"
    else:
        reprobados += 1
        categoria = "Reprobado"

    print(f"  {calif:>5.1f} → {categoria}")

print(f"\n=== Resumen ===")
print(f"Excelentes:  {excelentes}")
print(f"Buenos:      {buenos}")
print(f"Suficientes: {suficientes}")
print(f"Reprobados:  {reprobados}")
print(f"Total:       {len(calificaciones)}")
print(f"Promedio:    {sum(calificaciones) / len(calificaciones):.2f}")
