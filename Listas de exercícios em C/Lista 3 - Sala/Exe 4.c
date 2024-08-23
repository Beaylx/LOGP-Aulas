#include <stdio.h>

int main() {
    int N;
    
    printf("Digite um número menor ou igual a 50: ");
    scanf("%d", &N);
    
    if (N > 50) {
        printf("O número deve ser menor ou igual a 50.\n");
    } else {
        int produto = N;
        while (produto < 250) {
            printf("%d\n", produto);
            produto = produto * 3;
        }
    }
    
    return 0;
}