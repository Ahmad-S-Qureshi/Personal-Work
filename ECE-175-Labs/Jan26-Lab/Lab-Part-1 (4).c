/* This program will display the pair of inputs that multiply to the third input*/
#include <stdio.h>
#include <math.h>
int main(void) {
    int N;
    printf("Enter N: ");
    scanf("%d", &N);
    int RandN = (rand()%N) + 1;
    int input;
    printf("Enter a guess: ");
    scanf("%d", &input);
    while(input != RandN) {
        if(input > RandN){
            printf("%d is too high!\nTry again!\n", input);
        } else {
            printf("%d is too low!\nTry again!\n", input);
        }
        scanf("%d", &input);
    }
    printf("You got it!\n");
    return;
}