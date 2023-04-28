#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
#include <stdbool.h>

int rollDice(void){ 
// This function is to roll dice, calculate and return sum  // and display 
    int die1 = rand()%6 + 1;
    int die2 = rand()%6 + 1;
    printf("Player rolled %d + %d = %d\n", die1, die2, die1 + die2);  return die1 + die2; // return sum of dice 
}


int main(){
    srand((int)time(NULL)); // need only be applied once 
    bool playerDone = false;
    int playerPoint = 0;
    int currRoll = rollDice();
    char temp;
    while(!playerDone) {
        if(currRoll == 7 || currRoll == 11) {
            printf("Player wins\n");
            playerDone = true;
        } else {
            playerPoint = currRoll;
            printf("Point is %d\n", playerPoint);
            currRoll = rollDice();
            while (currRoll != playerPoint){
                currRoll = rollDice();
                if(currRoll == 7) {
                    playerDone = true;
                    printf("Player loses\n");
                    break;
                }
                printf("Hit enter to reroll\n");
                scanf("%c", &temp);
            }
            if(!playerDone) {
                printf("Player Wins!\n");
            }
            playerDone = true;
            
        }
    }

}