#include <stdio.h>
int main() 
{
float f,c,k;
printf("Enter Temperature in Fahrenheit\n");
scanf("%f",&f);
printf("Enter Temperature in Celsius\n");
scanf("%f",&c);
printf("Enter Temperature in Kelvin\n");
scanf("%f",&k);
float cel_fah=(c*1.8)+32;
float fah_cel=(f-32)*0.55555;
float kel_fah=1.8*(k-273.15) + 32;
float fah_kel=(f+459.67)*5/9;
float kel_cel = k - 273.15 ;         
float cel_kel=c+273.15;
printf("Temp from celsius to fahrenheit is:\t%f\n",cel_fah);
printf("Temp from fahrenheit to celsius is:\t%f\n",fah_cel);
printf("Temp from kelvin to fahrenheit is:\t%f\n",kel_fah);
printf("Temp from fahrenheit to kelvin is:\t%f\n",fah_kel);
printf("Temp from kelvin to celsius is:\t %f\n",kel_cel);
printf("Temp from celsius to kelvin is:\t %f\n",cel_kel);
return 0;
}
