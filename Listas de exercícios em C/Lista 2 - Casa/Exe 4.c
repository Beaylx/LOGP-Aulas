#include <stdio.h>

int main() {
    float N1, N2, N3;
    float maior, menor, NumeroDoMeio;

    printf("Digite o primeiro número: ");
    scanf("%f", &N1);
    printf("Digite o segundo número: ");
    scanf("%f", &N2);
    printf("Digite o terceiro número: ");
    scanf("%f", &N3);

    if (N1 >= N2 && N1 >= N3) {
        maior = N1;
    } else if (N2 >= N1 && N2 >= N3) {
        maior = N2;
    } else {
        maior = N3;
    }

    if (N1 <= N2 && N1 <= N3) {
        menor = N1;
    } else if (N2 <= N1 && N2 <= N3) {
        menor = N2;
    } else {
        menor = N3;
    }

    NumeroDoMeio = N1 + N2 + N3 - maior - menor;

    printf("O maior número é: %.2f\n", maior);
    printf("O menor número é: %.2f\n", menor);
    printf("O número do meio é: %.2f\n", NumeroDoMeio);

    return 0;
}