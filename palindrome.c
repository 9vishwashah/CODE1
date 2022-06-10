#include<stdio.h>
int main()
{
  int n;
  printf("Enter the length of string:\n");
  scanf("%d",&n);
  char s[n];
  printf("Enter the string:\n");
  scanf("%s",s);

  int p=1;
  for(int i=0;i<n/2;i++)
    {
      if (s[i]!=s[n-1-i])
      {
      p=0;
      break;
      }
    }
  
  if (p==1)
  {
    printf("It is a palindrome");
  }
  else
  {
    printf("It is not a palindrome");
  }
  return 0;
}
