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

    
    printf("Digite o número de horas trabalhadas no mês: ");
    scanf("%f", &horasTrabalhadas);

    printf("Digite o valor recebido por hora de trabalho: ");
    scanf("%f", &valorHora);

    printf("Digite o valor da contribuição ao INSS: ");
    scanf("%f", &inss);

    printf("Digite o número de dependentes (filhos menores de 14 anos): ");
    scanf("%d", &dependentes);

    printf("Digite o valor do salário família por dependente: ");
    scanf("%f", &salarioFamilia);

    
    salarioBruto = (horasTrabalhadas * valorHora) + (dependentes * salarioFamilia) - inss;

    
    printf("Salário bruto a ser recebido: R$ %.2f\n", salarioBruto);

    return 0;
}