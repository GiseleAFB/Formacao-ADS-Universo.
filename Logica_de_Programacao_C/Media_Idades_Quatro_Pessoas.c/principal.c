/******************************************************************************

Welcome to GDB Online.
  GDB online is an online compiler and debugger tool for C, C++, Python, PHP, Ruby, 
  C#, OCaml, VB, Perl, Swift, Prolog, Javascript, Pascal, COBOL, HTML, CSS, JS
  Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main() {
    char nomes[4][50]; // Array para armazenar os nomes das pessoas
    int idades[4];     // Array para armazenar as idades das pessoas
    int soma_idades = 0;
    float media_idades;

    // Solicita o nome e a idade de cada pessoa
    for (int i = 0; i < 4; i++) {
        printf("Digite o nome da pessoa %d: ", i + 1);
        scanf("%s", nomes[i]);

        printf("Digite a idade da pessoa %d: ", i + 1);
        scanf("%d", &idades[i]);

        soma_idades += idades[i]; // Adiciona a idade à soma total
    }

    // Calcula a média das idades
    media_idades = (float)soma_idades / 4;

    // Imprime a média das idades
    printf("\nA média das idades é: %.2f\n", media_idades);

    return 0;
}