#include <cs50.h>
#include <stdio.h>
int main(void)
{
    string x = get_string("what's your name?\n");
    printf("hello, %s\n", x);
}
