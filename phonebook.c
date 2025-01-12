#include <cs50.h>
#include <stdio.h>
#include <string.h>

typedef struct {
    string names;
    string number;
    }person;

int main(void)
{
    person people[3];

    people[0].names="basem";
    people[0].number="+216-96213215";
    people[1].names="fathia";
    people[1].number="+216-94703051";
    people[2].names="saleh";
    people[2].number="+216-98553457";



string name=get_string("Name: ");

for (int i=0;i<4;i++)
{
    if (strcmp(people[i].names,name)==0)
    {
    printf("Found%s\n",people[i].number);
    return 0;
    }
}

printf("Not found\n");
return 1;

}
