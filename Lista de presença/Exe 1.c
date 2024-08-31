#include <stdio.h>

int main() {
    char nome[100];
    float salarioAtual, novoSalario;
    int percentualAumento;

    printf("Digite seu nome: ");
    fgets(nome, sizeof(nome), stdin);

    printf("Digite o seu salário atual (R$): ");
    scanf("%f", &salarioAtual);

    if (salarioAtual <= 400.00) {
        percentualAumento = 15;
    } else if (salarioAtual <= 700.00) {
        percentualAumento = 12;
    } else if (salarioAtual <= 1000.00) {
        percentualAumento = 10;
    } else if (salarioAtual <= 1800.00) {
        percentualAumento = 7;
    } else if (salarioAtual <= 2500.00) {
        percentualAumento = 4;
    } else {
        percentualAumento = 0;
    }

    novoSalario = salarioAtual + (salarioAtual * percentualAumento / 100.0);

    printf("Informações do Funcionário:\n");
    printf("Nome: %s", nome);
    printf("Percentual de aumento: %d%%\n", percentualAumento);
    printf("Salário atual: R$ %.2f\n", salarioAtual);
    printf("Novo salário: R$ %.2f\n", novoSalario);

    return 0;
}