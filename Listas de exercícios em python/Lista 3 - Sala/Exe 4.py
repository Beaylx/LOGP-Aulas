N = int(input("Digite um número menor ou igual a 50: "))

if N > 50:
    print("O número deve ser menor ou igual a 50.")
else:
    produto = N
    while produto < 250:
        print(produto)
        produto = produto * 3