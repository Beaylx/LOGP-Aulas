prova1=float(input("Digite a nota da primeira prova: "))
prova2=float(input("Digite a nota da segunda prova: "))
atividade=float(input("Digite a nota da atividade: "))

media = (prova1*4+prova2*4+atividade*2)/10

print(f"A média semestral do aluno é: ", '%.2f' %media, ".")

