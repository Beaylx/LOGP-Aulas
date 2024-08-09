N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))
N3 = float(input("Digite o terceiro número: "))

maior = max(N1, N2, N3)
menor = min(N1, N2, N3)
NumeroDoMeio = N1 + N2 + N3 - maior - menor

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")
print(f"O número do meio é: {NumeroDoMeio}")