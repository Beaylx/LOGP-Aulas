nomes = list(('Ana', 'Carlos', 'Beatriz', 'Daniel', 'Elisa'))

if 'Carlos' in nomes:
    print('Carlos está na lista!')
else:
    print('Carlso não está na lista') 

nomes[2] = 'Bruna'

A = nomes.count('Ana')

print(nomes)
print(f'Ana aparece {A} vez na lista!')