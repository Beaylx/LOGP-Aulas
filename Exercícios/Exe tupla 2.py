cores = tuple(('Vermelho', 'Verde', "Azul"))

A = cores.index('Verde')

B = cores.count('Azul')

nova_tupla = cores + ('Branco', 'Cinza')


print(cores)
print(f'Indice da cor verde: {A}')
print(f'Azul aparece {B} vez')