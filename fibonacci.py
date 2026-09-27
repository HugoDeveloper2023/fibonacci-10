def es_primo(n):
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True


fib = [0, 1]
while len(fib) < 10:
    fib.append(fib[-1] + fib[-2])

print("Primeros 10 numeros de Fibonacci")
print("=" * 72)
print()
for i, n in enumerate(fib, 1):
    if i <= 2:
        origen = "valor inicial de la serie"
    else:
        origen = f"{fib[i - 3]} + {fib[i - 2]} = {n}"
    tipo = []
    if n == 0:
        tipo.append("cero")
    tipo.append("par" if n % 2 == 0 else "impar")
    if es_primo(n):
        tipo.append("primo")
    if n > 0 and int(n**0.5) ** 2 == n:
        tipo.append("cuadrado perfecto")
    detalle = ", ".join(tipo)
    print(f"  #{i:02d}  F({i - 1}) = {n:<4d}  |  {origen:<24}  |  {detalle}")

print()
print("Serie completa: " + " -> ".join(str(x) for x in fib))
print(f"Suma: {sum(fib)}")
print(f"Promedio: {sum(fib) / len(fib):.1f}")
