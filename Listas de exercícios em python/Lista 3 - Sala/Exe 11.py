maior = None
menor = None

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número inteiro: "))
    
    if maior is None or menor is None:
        maior = numero
        menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero

print(f"O maior valor é {maior}")
print(f"O menor valor é {menor}")