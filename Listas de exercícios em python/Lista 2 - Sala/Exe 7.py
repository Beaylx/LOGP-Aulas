numero = int(input("Digite um valor inteiro: "))

if numero < 0:
    ValorPositivo = numero * (-1)
    print(f"O valor em sua versão positiva é: {ValorPositivo}")

else:
    print(f"O valor {numero} já é positivo!")