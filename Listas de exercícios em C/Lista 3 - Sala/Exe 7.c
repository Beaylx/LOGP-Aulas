#include <stdio.h>

int main() {
    int base = 3;

    for (int i = 0; i <= 15; i++) {
        int potencia = 1; 
        
        for (int j = 0; j < i; j++) {
            potencia *= base;
        }
        
        printf("3 elevado a %d = %d\n", i, potencia);
    }
    
    return 0;
}