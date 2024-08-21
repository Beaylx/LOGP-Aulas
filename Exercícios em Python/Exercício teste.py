n=int(input('Digite um número inteiro e positivo!^^ :'))
conta_pares=0
conta_impares=0

for i in range(1,n+1):
    if i %2==0:
        conta_pares+=1
    else:
        conta_impares+=1

print(f'Total de números pares: {conta_pares}')
print(f'Total de números ímpares:{conta_impares}')