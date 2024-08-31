nome = input("Digite seu nome: ")
SalarioAtual = float(input("Digite o seu salário atual (R$): "))

NovoSalario = SalarioAtual
PercentualAumento = 0


if SalarioAtual <= 400.00:
    PercentualAumento = 15
elif SalarioAtual <= 700.00:
    PercentualAumento = 12
elif SalarioAtual <= 1000.00:
    PercentualAumento = 10
elif SalarioAtual <= 1800.00:
    PercentualAumento = 7
elif SalarioAtual <= 2500.00:
    PercentualAumento = 4
else:
    PercentualAumento = 0

NovoSalario = SalarioAtual + (SalarioAtual * PercentualAumento / 100)

print("Informações do Funcionário:")
print("Nome:", nome)
print("Percentual de aumento:", PercentualAumento, "%")
print("Salário atual: R$", SalarioAtual)
print(f"Novo salário: R$ {SalarioAtual:.2f}")