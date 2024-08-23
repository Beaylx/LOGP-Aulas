saldo=float(input("Insira seu saldo: "))

if saldo >= 1000:
    tarifa = saldo*0.8

if saldo >= 3000:
    tarifa = saldo*0.5
    
if saldo >= 5000:
    tarifa = saldo*0.25

print(f"A tarifa do seu saldo é: {tarifa:.2f}.")
