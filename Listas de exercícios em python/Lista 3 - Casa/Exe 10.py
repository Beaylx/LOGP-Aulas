while True:
    operacao = input("Digite uma operação (+, -, *, /) ou 'S' para sair: ").strip()

    if operacao == 'S':
        print("Saindo da calculadora. Até logo!")
        break
    
    if operacao in ['+', '-', '*', '/']:
        try:
            a = float(input("Digite o primeiro número (a): "))
            b = float(input("Digite o segundo número (b): "))

            if operacao == '+':
                resultado = a + b
                print(f"{a} + {b} = {resultado}")
            elif operacao == '-':
                resultado = a - b
                print(f"{a} - {b} = {resultado}")
            elif operacao == '*':
                resultado = a * b
                print(f"{a} * {b} = {resultado}")
            elif operacao == '/':
                if b != 0:
                    resultado = a / b
                    print(f"{a} / {b} = {resultado}")
                else:
                    print("Erro: Divisão por zero não é permitida.")
        except ValueError:
            print("Entrada inválida. Por favor, digite números válidos.")
    else:
        print("Operação inválida. Por favor, escolha uma das seguintes operações: +, -, *, / ou 'S' para sair.")