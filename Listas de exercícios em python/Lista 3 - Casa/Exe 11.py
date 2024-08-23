numero = int(input("Digite o número para a tabuada: "))

print(f"Tabuada do {numero}:")

for i in range(11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")