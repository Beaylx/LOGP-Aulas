TemperaturasC = [30, 25, 60, 80, 100]
TemperaturasF = [30, 25, 60, 80, 100]

def ConverterT (Temperaturas, Origem, Destino):

    if Origem == "C" and Destino == "F":
        return [Temp*9/5+32 for Temp in Temperaturas]

    elif Origem == "F" and Destino == "C":
        return [(Temp-32)*5/9 for Temp in Temperaturas]

    else:
        return 0

Origem = str(input("Insira seu parâmetro de origem baseado em C ou F"))

if Origem == "C":
    Destino = "F"

    ResultadoF = ConverterT(TemperaturasC, Origem, Destino)
    print (f"A converção para F equivale a: {ResultadoF}")

elif Origem == "F":
    Destino = "C"

    ResultadoC = ConverterT(TemperaturasF, Origem, Destino)
    print (f"A converção para C equivale a: {ResultadoC}")

else:
    print("Valor inválido!")
