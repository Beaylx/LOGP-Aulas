#include <stdio.h>

int main() {
    int numero;
    int maior = -2147483648;
    int menor = 2147483647;

    for (int i = 0; i < 5; i++) {
        printf("Digite o %dº número inteiro: ", i + 1);
        scanf("%d", &numero);

        if (numero > maior) {
            maior = numero;
        }
        if (numero < menor) {
            menor = numero;
        }
    }

    printf("O maior valor é %d\n", maior);
    printf("O menor valor é %d\n", menor);

    return 0;
}