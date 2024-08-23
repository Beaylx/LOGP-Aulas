#include <stdio.h>

double potencia(double base, int expoente) {
    double resultado = 1.0;
    
    for (int i = 0; i < expoente; i++) {
        resultado *= base;
    }
    
    return resultado;
}

int main() {
    double base;
    int expoente;

    printf("Digite a base (N): ");
    scanf("%lf", &base);
    
    printf("Digite o expoente (M): ");
    scanf("%d", &expoente);

    double resultado = potencia(base, expoente);
    
    printf("%.2f elevado a %d é igual a: %.2f\n", base, expoente, resultado);
    
    return 0;
}