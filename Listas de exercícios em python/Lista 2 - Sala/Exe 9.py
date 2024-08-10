N1 = int(input("Digite um número inteiro: "))
N2 = int(input("Insira um segundo número inteiro: "))

for numero in [N1, N2]:
    if numero % 5 == 0 and numero % 4 == 0:
        print(f"{numero} é divisível por 5 e 4.")
    elif numero % 5 == 0:
        print(f"{numero} é divisível apenas por 5.")
    elif numero % 4 == 0:
        print(f"{numero} é divisível apenas por 4.")
    else:
        print(f"{numero} não é divisível por 5 nem por 4.")