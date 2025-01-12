#include<cs50.h>
#include<stdio.h>
int add(int a,int b);
int main(void)
{
int x =get_int("give me x: ");
int y =get_int("give me y: ");

float z=(float)x/(float) y;
printf("%.2f\n",z);

}


