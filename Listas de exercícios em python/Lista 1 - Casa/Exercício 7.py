raio=float(input('Insira o raio da esfera: '))
pi = 3.141592653589793

volume= (4/3)*pi*(raio**3)
area= 4*pi*(raio**2)

print(f"O voulume da esféra é", '%.2f' %volume, "e sua área é", '%.2f' %area, "." )