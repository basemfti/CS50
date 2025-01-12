#include <cs50.h>
#include <stdio.h>

int calculate_quarters(int cents);
int calculate_dix(int cents);
int calculate_five(int cents);

int main(void)
{
    // Prompt the user for change owed, in cents
    int cents;

    do
    {
        cents = get_int("Change owed: ");
    }
    while (cents < 0);

    // Calculate how many quarters you should give customer
    int quarters = calculate_quarters(cents);


    // Subtract the value of those quarters from cents
    cents = cents - (quarters * 25);

     int x = calculate_dix(cents);
     int cents2 = cents - (x * 10);
    int y=calculate_five(cents2);
    int cents3 = cents2 - (y * 5);

    printf("%i\n",quarters+x+y+cents3);

}

int calculate_quarters(int cents)
{
    // Calculate how many quarters you should give customer
    int quarters = 0;
    while (cents >= 25)
    {
        quarters++;
        cents = cents - 25;
    }
    return quarters;
}
int calculate_dix(int cents)
{
    // Calculate how many quarters you should give customer
    int x = 0;
    while (cents >= 10)
    {
        x++;
        cents = cents - 10;
    }
    return x;
}
int calculate_five(int cents)
{
    // Calculate how many quarters you should give customer
    int y = 0;
    while (cents >= 5)
    {
        y++;
        cents = cents - 5;
    }
    return y;
}
