#include <stdio.h>

int main()
{
    float tarifa, saldo;
    printf("Insira seu saldo: ");
    scanf("%f",&saldo);
    
    if (saldo >= 1000) 
        tarifa = saldo*0.8;
    if (saldo >= 3000) 
        tarifa = saldo*0.5;
    if (saldo >= 5000) 
        tarifa = saldo*0.25;

    printf("A tarifa do seu saldo é: %2f", tarifa, ".");

    return 0;
}
