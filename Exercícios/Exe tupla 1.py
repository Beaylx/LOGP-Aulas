numeros = tuple((10, 20, 30, 40, 50))
A = numeros[3]

if 20 in numeros:
    print('O número 20 está presente na tupla!')
else:
    print('O número 20 não está presente na tupla.')

lista = list((numeros))

print(f'Terceiro número da tupla: {A}')
print(lista)