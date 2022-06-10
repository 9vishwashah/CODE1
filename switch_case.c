#include <stdio.h>
int main() 
{
     char c;
  double a, b;
  printf("Enter an operator (+, -, *, /): ");
  scanf("%c", &c);
  printf("Enter two operands: \n");
  scanf("%lf %lf", &a, &b);
  switch (c)
  {
    case '+':
      printf("%lf + %lf = %lf\n", a, b, a + b);
      break;
    case '-':
      printf("%lf - %lf = %lf\n", a, b, a - b);
      break;
    case '*':
      printf("%lf * %lf = %lf\n", a, b, a * b);
      break;
    case '/':
      printf("%lf / %lf = %lf\n", a, b, a / b);
      break;
    default:
    return 0;
  }
}
