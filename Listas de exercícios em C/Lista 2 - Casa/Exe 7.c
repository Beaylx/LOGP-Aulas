#include <stdio.h>

int main() {
    int codigo;

    printf("Digite o código de acesso (1 a 5): ");
    scanf("%d", &codigo);

    switch (codigo) {
        case 1:
            printf("Engenharia\n");
            break;
        case 2:
            printf("Edificações\n");
            break;
        case 3:
            printf("Sistemas Elétricos\n");
            break;
        case 4:
            printf("Turismo\n");
            break;
        case 5:
            printf("Análise de Sistemas\n");
            break;
        default:
            printf("Código inválido\n");
            break;
    }

    return 0;
}