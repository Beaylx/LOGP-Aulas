#include <stdio.h>

int main() {
    int numero = 2;
    do {
        printf("%d\n", numero);
        numero += 2;
    } while (numero <= 20);

    return 0;
}
