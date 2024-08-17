#include <stdio.h>

int main() {
    float nota;
    int ParteInteira;
    float resto;
    int NotaArredondada;

    printf("Insira nota do aluno: ");
    scanf("%f", &nota);

    ParteInteira = (int)nota;
    resto = nota - ParteInteira;

    if (resto > 0.5) {
        NotaArredondada = ParteInteira + 1;
    } else {
        NotaArredondada = ParteInteira;
    }

    printf("A nota arredondada do aluno é: %d.\n", NotaArredondada);

    return 0;
}