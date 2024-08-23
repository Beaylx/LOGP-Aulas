nota1=float(input('Digite sua primeira nota: '))
nota2=float(input('Digite sua segunda nota: '))

media=(nota1+nota2)/2

if media >= 6.0:
    print(f"Parabén você foi aprovado com {media:.2f} pontos de média")
else:
    exame=float(input('Você não foi aprovado! Digite sua nota do exame: '))
    novamedia=(nota1+nota2+exame)/3

    if novamedia >= 5.0:
        print(f'Você foi aprovado com {novamedia:.2f} pontos de média!')
    else:
        print(f'Você não foi aprovado com {novamedia:.2f} pontos de média!')

