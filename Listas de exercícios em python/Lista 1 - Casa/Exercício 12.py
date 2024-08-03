EspacoPercorrido=float(input("Digite o espaço percorrido (em km): "))
TempoGasto=float(input("Digite o tempo gasto (em horas): "))

VelocidadeMedia= EspacoPercorrido/TempoGasto

print(f"A velocidade mé do veículo é de: ",'%.2f' %VelocidadeMedia, "km/h.")