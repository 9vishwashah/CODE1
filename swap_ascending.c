#include <stdio.h>
int main()
{
    int a[10];
    printf("Enter 10 numbers\n");
    for (int i = 0; i < 10; i++) 
  {
    scanf("%d", &a[i]);
  }
    int s = 0;
    for (int i = 0; i < 10; i++) 
  {
    for (int j = 0; j < 10-1; j++) 
{
    if (a[j] > a[j+1]) 
  {
    int t = a[j];
    a[j] = a[j+1];
    a[j+1] = t;
    s++;
  }
}
    if (s == 0) 
  {
    break;
  }
  }
    for (int i = 0; i < 10; i++) 
    {
        printf("Ascending order is:\n%d ",a[i]);
    }
    printf("\n");
}
