#include <stdio.h>
#include <math.h>

int num(int n)
{
    int r = 0;
    while (n > 0) {
        int a = n % 10;
        r= r * 10 + a;
        n /= 10;
    }
    return r;
}

int main()
{
    int n;
    printf("Enter a number: ");
    scanf("%d", &n);

    printf("After reversal: %d\n", num(n));
}
