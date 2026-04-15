/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/

#include <stdio.h>

int main() {
    float horasTrabalhadas, valorHora, inss, salarioFamilia, salarioBruto;
    int dependentes;

    printf("Digite o número de horas trabalhadas: ");
    scanf("%f", &horasTrabalhadas);
    printf("Digite o valor recebido por hora: ");
    scanf("%f", &valorHora);
    printf("Digite o valor da contribuição ao INSS: ");
    scanf("%f", &inss);
    printf("Digite o número de dependentes: ");
    scanf("%d", &dependentes);
    printf("Digite o valor do salário família por dependente: ");
    scanf("%f", &salarioFamilia);

    
    salarioBruto = (horasTrabalhadas * valorHora) + (dependentes * salarioFamilia);

    
    salarioBruto -= inss;

    printf("Salário bruto: %.2f\n", salarioBruto);

    return 0;
}