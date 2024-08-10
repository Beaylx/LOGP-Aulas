nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('Dgite a segunda nota: '))
nota3 = float(input('Digite a terceira nota: '))

media = (nota1+nota2+nota3)/3

if media >= 6.0:
    print(f"Parabén!! Você foi aprovado com {media:.2f}.")
else:
    print(f"Você não foi aprovado com {media:.2f}.")