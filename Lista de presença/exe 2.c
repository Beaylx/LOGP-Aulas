#include <stdio.h>

int main() {
    float soma = 0;
    int totalElementos = 0;
    float maior = -1e30;
    float menor = 1e30;
    int faixa1 = 0, faixa2 = 0, faixa3 = 0, faixa4 = 0, faixa5 = 0;
    float somaFaixa1 = 0, somaFaixa2 = 0, somaFaixa3 = 0, somaFaixa4 = 0, somaFaixa5 = 0;
    int pares = 0, impares = 0;
    float valor;
    char continuar;

    while (1) {
        printf("Digite um valor (ou 'sair' para encerrar): ");
        if (scanf("%f", &valor) != 1) {
            while (getchar() != '\n');
            printf("Entrada inválida. Digite 'sair' para encerrar ou um valor numérico.\n");
            continue;
        }

        soma += valor;
        totalElementos++;

        if (valor > maior) {
            maior = valor;
        }
        if (valor < menor) {
            menor = valor;
        }

        if (valor < 0) {
            faixa1++;
            somaFaixa1 += valor;
        } else if (valor >= 0 && valor < 15) {
            faixa2++;
            somaFaixa2 += valor;
        } else if (valor >= 15 && valor < 100) {
            faixa3++;
            somaFaixa3 += valor;
        } else if (valor >= 100 && valor < 1000) {
            faixa5++;
            somaFaixa5 += valor;
        } else {
            faixa4++;
            somaFaixa4 += valor;
        }

        if ((int)valor % 2 == 0) {
            pares++;
        } else {
            impares++;
        }

        printf("Deseja continuar? (s/n): ");
        scanf(" %c", &continuar);
        if (continuar != 's' && continuar != 'S') {
            break;
        }
    }

    float media = (totalElementos > 0) ? soma / totalElementos : 0;

    printf("\nMédia aritmética dos valores: %.2f\n", media);
    printf("Maior valor: %.2f\n", maior);
    printf("Menor valor: %.2f\n", menor);
    printf("Total de elementos por faixa:\n");
    printf("Faixa 1 (< 0): %d, Total: %.2f\n", faixa1, somaFaixa1);
    printf("Faixa 2 (0 <= valor < 15): %d, Total: %.2f\n", faixa2, somaFaixa2);
    printf("Faixa 3 (15 <= valor < 100): %d, Total: %.2f\n", faixa3, somaFaixa3);
    printf("Faixa 4 (>= 1000): %d, Total: %.2f\n", faixa4, somaFaixa4);
    printf("Faixa 5 (100 <= valor < 1000): %d, Total: %.2f\n", faixa5, somaFaixa5);
    printf("Total de pares: %d\n", pares);
    printf("Total de ímpares: %d\n", impares);

    return 0;
}