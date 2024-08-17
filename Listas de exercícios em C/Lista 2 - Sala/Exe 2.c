#include <stdio.h>

int main() {
    float N1, N2, M, E, NV;

    printf("Insira sua primeira nota: ");
    scanf("%f", &N1);
    printf("Insira sua segunda nota: ");
    scanf("%f", &N2);

    M = (N1 + N2) / 2;

    if (M >= 6.0) {
        printf("Parabéns! Você foi aprovado com a média: %.2f\n", M);
    } else {

        printf("Você não foi aprovado! Insira sua nota do exame: ");
        scanf("%f", &E);

        NV = (M + E) / 2;

        if (NV >= 5.0) {
            printf("Você foi aprovado com a média: %.2f\n", NV);
        } else {
            printf("Você não foi aprovado\n");
        }
    }

    return 0;
}