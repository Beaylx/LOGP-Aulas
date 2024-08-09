nota = float(input("Insira nota do aluno: "))

ParteInteira = int(nota)
resto = nota - ParteInteira

if resto > 0.5:
    NotaArredondada = ParteInteira + 1
else:
    NotaArredondada = ParteInteira

print(f"A nota arredondada do aluno é: {NotaArredondada}.")


