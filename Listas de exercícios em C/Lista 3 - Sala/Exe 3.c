#include <stdio.h>

int main() {
    int numero;

    printf("Digite o número para gerar a tabuada: ");
    scanf("%d", &numero);

    for (int i = 1; i <= 10; i++) {
        int resultado = numero * i;
        printf("%d X %d = %d\n", numero, i, resultado);
    }
    
    return 0;
}