/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>

int main()
{ 
    char nome1[50],nome2 [50];
    int idade1, idade2;
    
    printf("digite o nome da primeira pessoa:"); 
    scanf("%s",nome1);
    printf("digite a idade da primeira pessoa:");
scanf("%d",&idade1);

printf("digite o nome da segunda pessoa:");
scanf("%s",nome2);
printf("digite a idade da segunda pessoa");
scanf("%d",&idade2);

printf ("\ndados da pesssoa:\n");
printf ("nome:%s,idade:%d\n",nome1,idade1);
printf ("nome:%s,idade:%d\n",nome2,idade2);


    return 0;
}