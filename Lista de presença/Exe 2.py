soma = 0
TotalElementos = 0
maior = float('-inf')
menor = float('inf')
faixa1 = faixa2 = faixa3 = faixa4 = faixa5 = 0
SomaFaixa1 = SomaFaixa2 = SomaFaixa3 = SomaFaixa4 = SomaFaixa5 = 0
pares = 0
impares = 0

while True:
    valor = float(input("Digite um valor (ou 'sair' para encerrar): "))
    
    soma += valor
    TotalElementos += 1
    
    if valor > maior:
        maior = valor
    if valor < menor:
        menor = valor
    
    if valor < 0:
        faixa1 += 1
        SomaFaixa1 += valor
    elif 0 <= valor < 15:
        faixa2 += 1
        SomaFaixa2 += valor
    elif 15 <= valor < 100:
        faixa3 += 1
        SomaFaixa3 += valor
    elif 100 <= valor < 1000:
        faixa5 += 1
        SomaFaixa5 += valor
    else:
        faixa4 += 1
        SomaFaixa4 += valor

    if valor % 2 == 0:
        pares += 1
    else:
        impares += 1

    continuar = input("Deseja continuar? (s/n): ").strip().lower()
    if continuar != 's':
        break

if TotalElementos > 0:
    media = soma / TotalElementos
else:
    media = 0

print(f"\nMédia aritmética dos valores: {media:.2f}")
print(f"Maior valor: {maior}")
print(f"Menor valor: {menor}")
print(f"Total de elementos por faixa:")
print(f"Faixa 1 (< 0): {faixa1}, Total: {SomaFaixa1:.2f}")
print(f"Faixa 2 (0 <= valor < 15): {faixa2}, Total: {SomaFaixa2:.2f}")
print(f"Faixa 3 (15 <= valor < 100): {faixa3}, Total: {SomaFaixa3:.2f}")
print(f"Faixa 4 (>= 1000): {faixa4}, Total: {SomaFaixa4:.2f}")
print(f"Faixa 5 (100 <= valor < 1000): {faixa5}, Total: {SomaFaixa5:.2f}")
print(f"Total de pares: {pares}")
print(f"Total de ímpares: {impares}")