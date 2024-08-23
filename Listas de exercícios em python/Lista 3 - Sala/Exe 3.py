numero = int(input("Digite o número para gerar a tabuada: "))

for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} X {i} = {resultado}")