/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/
#include <stdio.h>
#include <string.h>

int main() {
    char nome[100];
    int idade;
    char sexo;
    float peso;
    float altura;
    char profissao[100];
    char rua[100];
    char bairro[100];
    char cidade[100];
    char estado[3];
    char cep[10];
    char telefone[20];

    // Leitura das informações
    printf("Digite o nome: ");
    fgets(nome, sizeof(nome), stdin);
    nome[strcspn(nome, "\n")] = 0; // Remove o caractere de nova linha

    printf("Digite a idade: ");
    scanf("%d", &idade);
    getchar(); // Limpa o buffer do teclado

    printf("Digite o sexo (M/F): ");
    scanf("%c", &sexo);
    getchar();

    printf("Digite o peso: ");
    scanf("%f", &peso);
    getchar();

    printf("Digite a altura: ");
    scanf("%f", &altura);
    getchar();

    printf("Digite a profissão: ");
    fgets(profissao, sizeof(profissao), stdin);
    profissao[strcspn(profissao, "\n")] = 0;

    printf("Digite a rua: ");
    fgets(rua, sizeof(rua), stdin);
    rua[strcspn(rua, "\n")] = 0;

    printf("Digite o bairro: ");
    fgets(bairro, sizeof(bairro), stdin);
    bairro[strcspn(bairro, "\n")] = 0;

    printf("Digite a cidade: ");
    fgets(cidade, sizeof(cidade), stdin);
    cidade[strcspn(cidade, "\n")] = 0;

    printf("Digite o estado (UF): ");
    fgets(estado, sizeof(estado), stdin);
    estado[strcspn(estado, "\n")] = 0;

    printf("Digite o CEP: ");
    fgets(cep, sizeof(cep), stdin);
    cep[strcspn(cep, "\n")] = 0;

    printf("Digite o telefone: ");
    fgets(telefone, sizeof(telefone), stdin);
    telefone[strcspn(telefone, "\n")] = 0;

    // Exibição das informações
    printf("\nInformações da Pessoa:\n");
    printf("Nome: %s\n", nome);
    printf("Idade: %d\n", idade);
    printf("Sexo: %c\n", sexo);
    printf("Peso: %.2f kg\n", peso);
    printf("Altura: %.2f m\n", altura);
    printf("Profissão: %s\n", profissao);
    printf("Endereço: %s, %s, %s - %s, CEP: %s\n", rua, bairro, cidade, estado, cep);
    printf("Telefone: %s\n", telefone);

    return 0;
}
