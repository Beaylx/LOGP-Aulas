AlturaParede=float(input('Insira a altura da parede: '))
LarguraParede =float(input('Insira a largura da parede: '))

AlturaAzulejo=float (input('Insira a altura dos azulejos: '))
LarguraAzulejo=float(input('Insira a largura do azulejos: '))

AzulejosNecessarios = (AlturaParede*LarguraParede)/(AlturaAzulejo*LarguraAzulejo)

print(f"O números de azulejos necessários é:", '%.2f' %AzulejosNecessarios,)