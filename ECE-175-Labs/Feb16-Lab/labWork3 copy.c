#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
void main() {
    FILE* currFile = fopen("flights.txt", "r");
    FILE* writeFile = fopen("flights2.txt", "w");
    char inputLetter1;
    char inputLetter2;
    int inputNum;
    char letter1;
    char letter2;
    int number;
    char type;
    int flag = 0;
    scanf("%c%c%*c%d", &inputLetter1, &inputLetter2, &inputNum);
    while(fscanf(currFile, "%c%c%d%*c%c%*c", &letter1, &letter2, &number, &type) != EOF){
        if(letter1 == inputLetter1 && letter2 == inputLetter2 && number == inputNum) {
            if(type == 'L') {
                printf("Flight has landed");
                
                flag = 1;
            } else if (type =='D') {
                printf("Flight has departed");
                
                flag = 1;
            } else {
                printf("Flight has been cancelled");
                printf("%c", type);
                flag = 1;
            }
            flag = 1;
        }
        fprintf(writeFile, "%c%c %d %c\n", letter1, letter2, number, type);
    }
    if(flag ==0) {
        printf("write L for landed, D for departed, and C for cancelled\n");
        scanf("%*c%c", &type);
        fprintf(writeFile, "%c%c %d %c\n", letter1, letter2, number, type);
        return;
    }
    return;
}
