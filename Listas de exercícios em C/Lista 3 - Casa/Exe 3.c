#include <stdio.h>

int main() {
    int numero = 1;

    while (numero <= 20) {
        if (numero % 2 == 0) {
            printf("%d é par\n", numero);
        } else {
            printf("%d é ímpar\n", numero);
        }
        numero++;
    }

    return 0;
}