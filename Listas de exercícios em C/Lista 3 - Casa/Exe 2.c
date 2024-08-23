#include <stdio.h>

int main() {
    int numero = 20;

    while (numero >= 1) {
        if (numero % 2 == 0) {
            printf("%d\n", numero);
        }
        numero--;
    }

    return 0;
}