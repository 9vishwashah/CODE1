#include <stdio.h>
#include<string.h>
int main() 
{
  char s1[50];
  char s2[50];
  printf("Enter the First string\n");
  scanf("%s",s1);
  printf("Enter the second string\n");
  scanf("%s",s2);
  printf("Length of first string:%lu\n",strlen(s1));
  printf("Length of second string:%lu\n",strlen(s2));
 if (strcmp(s1,s2)==0)
{
 printf("String are Same\n");
}
 else
{
 printf("Strings are not same\n");
}
 printf("Concatinating Two string:%s\n",strcat(s1,s2));
 printf("Copying Two String: %s\n",strcpy(s1,s2));
 return 0;
}
  
  
