#include <stdio.h>
int main()
{
    int n;
    printf("Enter leap year: ");
    scanf("%d", &n);
    if (n % 400 == 0) 
    {
        printf("It is a leap year\n");
    } 
    else if (n % 100 == 0) 
    {
        printf("It is not a leap year\n");
    } 
    else if (n % 4 == 0) 
    {
        printf("It is a leap year\n");
    } 
    else 
    {
        printf("It is not a leap year\n");
    }
}
