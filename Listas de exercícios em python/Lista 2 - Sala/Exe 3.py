valor1 = float(input('Digite o primeiro valor: '))
valor2 = float(input('Digite o segundo valor: '))

if valor1 > valor2:
    diferença = valor1-valor2
else:
    diferença = valor2-valor1

print(f"A diferença entre os números é {diferença:.2f}.")
