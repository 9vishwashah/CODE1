#include <stdio.h>
int fact(int);
int main() 
{
    int n;
    printf("Enter the number:\n");
    scanf("%d",&n);
    int f=fact(n);
    printf("Factorial = %d",f);
}
  int fact(int n)
{
  if (n==0)
{
    return 0;
}
  else if (n==1)
{
    return 1;
}
  else 
{
    return n*fact(n-1);
}
 return 0;
}
  
