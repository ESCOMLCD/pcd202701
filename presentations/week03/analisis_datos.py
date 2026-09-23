# Análisis de datos con estructuras de Python
# Este script simula el tipo de análisis que harán en la Práctica 1

# Datos simulados (en la práctica vendrán de un CSV)
registros = [
    {"producto": "Laptop",    "monto": 15000, "email": "ana@gmail.com"},
    {"producto": "Mouse",     "monto": 350,   "email": "luis@hotmail.com"},
    {"producto": "Laptop",    "monto": 14500, "email": "carlosgmail.com"},
    {"producto": "Teclado",   "monto": 800,   "email": ""},
    {"producto": "Monitor",   "monto": 5000,  "email": "sofia@yahoo.com"},
    {"producto": "Laptop",    "monto": 15500, "email": "diego@@live.com"},
    {"producto": "Mouse",     "monto": 400,   "email": "val@outlook.com"},
    {"producto": "Impresora", "monto": 3500,  "email": "andrea@gmail.com"},
    {"producto": "Mouse",     "monto": 320,   "email": "miguel@"},
    {"producto": "Laptop",    "monto": 16000, "email": "paula@gmail.com"},
]

# 1. Dimensiones
print(f"=== Resumen del Dataset ===")
print(f"Total de registros: {len(registros)}")
print(f"Columnas: {list(registros[0].keys())}")

# 2. Valores únicos de la categórica
productos_unicos = set(r["producto"] for r in registros)
print(f"\nProductos únicos: {len(productos_unicos)} → {productos_unicos}")

# 3. Conteo por categoría
conteo = {}
for r in registros:
    prod = r["producto"]
    conteo[prod] = conteo.get(prod, 0) + 1

print(f"\nConteo por producto:")
for prod, n in sorted(conteo.items(), key=lambda x: x[1], reverse=True):
    print(f"  {prod}: {n}")

mas_frecuente = max(conteo, key=conteo.get)
print(f"Más frecuente: {mas_frecuente} ({conteo[mas_frecuente]} veces)")

# 4. Estadísticas de la numérica
montos = [r["monto"] for r in registros]
print(f"\nEstadísticas de monto:")
print(f"  Mínimo:   ${min(montos):,}")
print(f"  Máximo:   ${max(montos):,}")
print(f"  Promedio: ${sum(montos) / len(montos):,.2f}")

# 5. Calidad de datos — emails vacíos o sospechosos
vacios = sum(1 for r in registros if r["email"].strip() == "")
sin_arroba = sum(1 for r in registros if "@" not in r["email"] and r["email"].strip() != "")
print(f"\nCalidad de emails:")
print(f"  Vacíos: {vacios}")
print(f"  Sin @:  {sin_arroba}")
