soma = 0

for numero in range(1, 501):
    if numero % 2 == 0:
        soma += numero

print(f"A soma dos valores pares de 1 até 500 é {soma}")