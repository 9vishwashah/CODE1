#include <stdio.h>
int main()
{
    int a, b;
    printf("Enter two positive integers:\n ");
    scanf("%d %d",&a,&b);
    while(a!=b)
{
  if(a > b)
  a -= b;
  else
  b -= a;
}
  printf("GCD = %d",a);
  return 0;
}
