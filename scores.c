#include<cs50.h>
#include<stdio.h>
#include<string.h>



int main(void )
{
string s =get_string("what's your name: ");
printf("output:");

for (int i=0,  n = strlen(s);i<n; i++)
{
    printf("%c",s[i]);


}
printf("\n");
    }




