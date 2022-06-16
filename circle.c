#include <stdio.h>
int main()
{
    double r;
    printf("Enter radius:\n");
    scanf("%lf", &r);
    double c= 2 * 3.141592653589793238 * r;
    double d= 2*r;
    double a = 3.141592653589793238 * r * r;
    printf("Circumference of Circle: %lf\n", c);
    printf("Area of Circle:          %lf\n", a);
    printf("Diameter of Circle:      %lf\n",d);
}
