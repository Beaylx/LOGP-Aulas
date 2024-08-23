#include <stdio.h>

int main() {
    for (int numero = 20; numero > 0; numero--) {
        if (numero % 2 == 0) {
            printf("%d é par\n", numero);
        } else {
            printf("%d é ímpar\n", numero);
        }
    }

    return 0;
}