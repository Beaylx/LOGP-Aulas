raio=float(input("Digite o valor do raio da lata de óleo (em metros): "))
altura=float(input("Digite o valor da altura da lata de óleo (em metros): "))

volume= 3.14159*(raio**2)*altura

print(f"O volume da lata de oléo é de",'%.2f' %volume, "metros cubicos.")