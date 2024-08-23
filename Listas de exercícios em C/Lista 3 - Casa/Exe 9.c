#include <stdio.h>

int main() {
    int numero = 1;

    while (1) { 
        if (numero % 2 == 0) {
            printf("%d é par\n", numero);
        } else {
            printf("%d é ímpar\n", numero);
        }

        numero++;

        if (numero > 20) {
            break;
        }
    }

    return 0;
}