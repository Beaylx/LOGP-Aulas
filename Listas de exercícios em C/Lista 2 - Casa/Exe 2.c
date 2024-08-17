#include <stdio.h>
#include <stdlib.h> 

int main() {
    int numero;
    int NumeroChave = 35;

    printf("Digite um número inteiro (0 a 100): ");
    scanf("%d", &numero);

    if (numero >= 0 && numero <= 100) {

        int distancia = abs(NumeroChave - numero);

        printf("Distância entre %d e %d é %d.\n", numero, NumeroChave, distancia);
    } else {
       
        printf("Número fora dos limites! Tente novamente (apenas entre 0 a 100).\n");
    }

    return 0;
}