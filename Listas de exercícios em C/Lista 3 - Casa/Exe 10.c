#include <stdio.h>

int main() {
    char operacao;
    float a, b, resultado;
    
    while (1) {
        printf("Digite uma operação (+, -, *, /) ou 'S' para sair: ");
        scanf(" %c", &operacao);

        if (operacao == 'S' || operacao == 's') {
            printf("Saindo da calculadora. Até logo!\n");
            break;
        }

        if (operacao == '+' || operacao == '-' || operacao == '*' || operacao == '/') {
            printf("Digite o primeiro número (a): ");
            if (scanf("%f", &a) != 1) {
                printf("Entrada inválida para o primeiro número.\n");
                while (getchar() != '\n');
                continue;
            }
            printf("Digite o segundo número (b): ");
            if (scanf("%f", &b) != 1) {
                printf("Entrada inválida para o segundo número.\n");
                while (getchar() != '\n');
                continue;
            }

            if (operacao == '+') {
                resultado = a + b;
                printf("%.2f + %.2f = %.2f\n", a, b, resultado);
            } else if (operacao == '-') {
                resultado = a - b;
                printf("%.2f - %.2f = %.2f\n", a, b, resultado);
            } else if (operacao == '*') {
                resultado = a * b;
                printf("%.2f * %.2f = %.2f\n", a, b, resultado);
            } else if (operacao == '/') {
                if (b != 0) {
                    resultado = a / b;
                    printf("%.2f / %.2f = %.2f\n", a, b, resultado);
                } else {
                    printf("Erro: Divisão por zero não é permitida.\n");
                }
            }
        } else {
            printf("Operação inválida. Por favor, escolha uma das seguintes operações: +, -, *, / ou 'S' para sair.\n");
        }
        
        while (getchar() != '\n');
    }

    return 0;
}