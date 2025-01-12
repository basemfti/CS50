#include <ctype.h>
#include <cs50.h>
#include <math.h>
#include <stdio.h>
#include <string.h>
int letters(string text);
int words(string text);
int sentences(string text);


int main(void)
{
    string text=get_string("Text: ");

    int leter=letters(text);
    int word=words(text);
    int sent=sentences(text);
    double l=leter/(float)word*100;

    double s=sent/(float)word*100;
    int index =round( 0.0588 *l- 0.296 * s - 15.8);

    if (index >16)
    printf("Grade 16+\n");
    else if (index<1)
    printf("Before Grade 1\n");
    else
    printf("Grade %i\n",index);

}


int letters(string ch)

{
    int j=0;

    for (int i=0;i<strlen(ch);i++)
    {
        if (isalpha(ch[i])!=0)

        j++;

    }
    return j;
}
int words(string ch)
{
    int j=1;
   for (int i=0;i<strlen(ch);i++)
   {
    if (ch[i]==' ')
    {
        j++;
    }
   }
   return j;
   }


int sentences(string ch)
{
    int j=0;
   for (int i = 0;i<strlen(ch); i++)
   {
    if (ch[i]=='!' || ch[i]=='.'|| ch[i]=='?')
    {
        j++;
    }
   }
   return j;
   }
