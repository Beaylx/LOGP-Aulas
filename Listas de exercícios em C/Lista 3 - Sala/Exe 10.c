#include <stdio.h>

int main() {
    int soma = 0;

    for (int numero = 1; numero <= 500; numero++) {
        if (numero % 2 == 0) {
            soma += numero;
        }
    }

    printf("A soma dos valores pares de 1 até 500 é %d\n", soma);

    return 0;
}