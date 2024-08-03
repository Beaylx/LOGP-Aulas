valor=float(input("Digite o valor da prestação: "))
taxa=float(input("Digite a taxa de juros (em %): "))
tempo=float(input("Digite o tempo em atraso (em meses): "))

PrestacaoAtrasada= valor+(valor*(taxa/100)*tempo)

print(f"O valor da prestação em atraso é de:",'%.2f' %PrestacaoAtrasada, "R$.")