#include<stdio.h>
#include<cs50.h>
#include<ctype.h>
#include<string.h>

int main(void)
{
string s =get_string("Before: ");
printf("after:");

for (int i=0,n=strlen(s);i<n;i++)
{


    printf("%c",toupper (s[i]));
}
printf("\n");


}
