#include<stdio.h>
#include<cs50.h>


int main(void )
{
    //Promt the user to put a postive integer
    int n;
    do
    {
        n=get_int("size: ");
    }
    while (n<1);
    for (int i=0;i<n;i++)
    {
//print n*n bricks
    for(int j=0;j<n;j++)
    {
         printf("#");



    }
    printf("\n");
    }




}
