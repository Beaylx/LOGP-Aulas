ladoB=float(input('Insira o tamanho do lado B do retângulo: '))
LadoA=float (input('Insira o tamanho do lado A do retângulo: '))

Área= ladoB*LadoA
Perimetro= (2*LadoA)+(2*ladoB)

print(f"O retângulo possui um perímetro de",'%.2f' %Perimetro, "cm e área de",'%.2f' %Área, "cm.")