#include<cs50.h>
#include<stdio.h>
#include<string.h>



int main(void)
{
    string strings[]={"basem","hakim","bes","ferdaws","fatha","salah","lbes"};
    string ch=get_string("give me ur name:");
    for (int i=0;i<7;i++)
    {
        if (strcmp(strings[i],ch)==0)
        {
            printf("we find yur name here: %i\n",i+1);
            return 0;
        }

    }
    printf("Not found\n");
    return 1;


}
