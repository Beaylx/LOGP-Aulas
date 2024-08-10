import math

A = float(input("Digite um primeiro valor: "))
B = float(input("Digite um segundo valor: "))
C = float(input("Digite um terceiro valor: "))

delta = B**2 - 4*A*C

if delta > 0:
    raiz1 = (-B + math.sqrt(delta)) / (2*A)
    raiz2 = (-B - math.sqrt(delta)) / (2*A)
    print(f"As raízes são: {raiz1} e {raiz2}")
    
else:
    print("Não há raízes reais.")

