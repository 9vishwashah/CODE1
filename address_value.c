#include <stdio.h>
int main()
{
    int n = 3;
    int *p = &n;
    printf("Value of n is: %d\n", n);
    printf("Address of n is: %x\n", &n);
    printf("Value of ptr is: %x\n", p);
    printf("Value at ptr is: %d\n", *p);
}
