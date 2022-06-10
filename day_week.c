#include <stdio.h>

int main()
{
    int a;
    printf("Enter number of day:\n");
    scanf("%d", &a);
    if (a == 1) 
    {
        printf("Monday\n");
    } 
    else if (a == 2) 
    {
        printf("Tuesday\n");
    } 
    else if (a == 3) 
    {
        printf("Wednesday\n");
    } 
    else if (a == 4) 
    {
        printf("Thursday\n");
    } 
    else if (a == 5) 
    
        printf("Friday\n");
    } 
    else if (a == 6) 
    {
        printf("Saturday\n");
    } 
    else if (a == 7) 
    {
        printf("Sunday\n");
    } 
    else 
    {
        printf("Invalid input\n");
    }
}
