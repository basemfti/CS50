#include<stdio.h>
#include<cs50.h>
#include<string.h>
#include<ctype.h>
int scrable(string x);
int points[]={1,3,3,2,1,4,2,4,1,8,5,1,3,1,1,3,10,1,1,1,1,4,4,8,4,10};


int main (void)
{
string player1=get_string("player1: ");
string player2=get_string("player2: ");

int x=scrable(player1);
int y=scrable(player2);
if (x>y)
{
    printf("player 1 wins\n");

}
else if (x<y)
    {
        printf("player 2 wins\n ");

    }

else
   printf("Ties!\n ");
}



int scrable(string x)
{
int score=0;
    for (int i=1;i<=strlen(x);i++)

    {
        if (isupper(x[i]))
        {
            score+=points[x[i]-'A'];


        }
        else if (islower(x[i]))
        {
             score+=points[x[i]-'a'];

        }

    }
return score;
}
