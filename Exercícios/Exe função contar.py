def ContarC(texto):
    Frequencia = {}

    for Caractere in texto:

        if Caractere != "":
            if Caractere in Frequencia:
                Frequencia[Caractere] += 1
            else:
                Frequencia[Caractere] = 1
    return Frequencia

texto = str(input("Insira seu texto: "))
Contagem = ContarC(texto)
print (Contagem)