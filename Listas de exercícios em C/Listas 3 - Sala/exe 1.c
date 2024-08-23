#include <stdio.h>

int main() {
    for (int numero = 0; numero < 21; numero++) 
        if (numero % 2 != 0) 
            printf("%d\n", numero);
    
    return 0;
}