#include<cs50.h>
#include<stdio.h>
#include<string.h>
#include<ctype.h>
#include<stdlib.h>

int main(void)
{
    char *s=get_string("s:");


    char *a= malloc(strlen(s)+1);

   strcpy(a,s);


    if (strlen(s)>0)
    {
    s[0]=toupper(s[0]);
    }

    printf("%s\n",s);
    printf("%s\n",a);
    free(a);



}


