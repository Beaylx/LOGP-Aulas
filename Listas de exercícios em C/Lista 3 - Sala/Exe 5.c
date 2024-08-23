#include <stdio.h>

int main() {
    int contador = 1;
    
    while (contador < 200) {
        if (contador % 4 == 0) {
            printf("%d\n", contador);
        }
        contador++;
    }
    
    return 0;
}