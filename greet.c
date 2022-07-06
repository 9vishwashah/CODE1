#include<stdio.h>

void goodMorning();

void goodAfternoon();

void goodNight();

int main(){

    goodMorning();

    return 0;

}

void goodMorning(){

    printf("Good Morning Vishwa\n");

    goodAfternoon();

}

void goodAfternoon(){

    printf("Good Afternoon vishwa\n");

    goodNight();

}

void goodNight(){

    printf("Good Night Vishwa\n");

}

