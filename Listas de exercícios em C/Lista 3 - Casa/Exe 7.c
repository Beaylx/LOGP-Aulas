#include <stdio.h>

int main() {
    int numero = 1;

    while (1) {
        if (numero % 2 == 0) {
            printf("%d\n", numero);
        }
        numero++;

        if (numero > 20) {
            break;
        }
    }

    return 0;
}