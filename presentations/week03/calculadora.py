# Calculadora simple

print("=== Calculadora ===")
num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))

print(f"\nResultados:")
print(f"  {num1} + {num2} = {num1 + num2}")
print(f"  {num1} - {num2} = {num1 - num2}")
print(f"  {num1} * {num2} = {num1 * num2}")

if num2 != 0:
    print(f"  {num1} / {num2} = {num1 / num2:.2f}")
else:
    print("  División entre cero no permitida")
