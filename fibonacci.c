#include <stdio.h>
int main()
{
  int n,a=0,b=1;
  int c=a+b;
  printf("Enter number of terms:\n");
  scanf("%d",&n);
  printf("Fibonnaaci Series: \n%d\n%d\n",a,b);
  for(int i=3;i<=n;++i)
{
  printf("%d\n",c);
  a=b;
  b=c;
  c=a+b;
}
return 0;
}
  
