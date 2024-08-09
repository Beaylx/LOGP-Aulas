numero = int(input("Digite um número inteiro (0 a 100): "))
NumeroChave = 35

if 0 <= numero <= 100:
    distancia = abs(NumeroChave-numero)
    print(f"Distancia entre {numero} e {NumeroChave} é {distancia}.")
else:
    print("Número fora dos limites! tente novamente (apenas entre 0 a 100).")
    