N1 = int(input("Digite um número inteiro: "))
N2 = int(input("Insira um segundo número inteiro: "))
N3 = int(input("Insira um terceiro númeor inteiro: "))

for numero in [N1, N2, N3]:
    if numero % 2 == 0 and numero % 3 == 0:
        print(f"{numero} é divisível por 2 e 3.")
    elif numero % 2 == 0:
        print(f"{numero} é divisível apenas por 2.")
    elif numero % 3 == 0:
        print(f"{numero} é divisível apenas por 3.")
    else:
        print(f"{numero} não é divisível por 2 nem por 3.")