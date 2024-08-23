#include <stdio.h>

int main() {
    int a = 1;
    int b = 1;
    int contador = 1;
    
    while (contador <= 15) {
        printf("%d\n", a); 
        
        int temp = a;
        a = b;
        b = temp + b;
        
        contador++;
    }
    
    return 0;
}