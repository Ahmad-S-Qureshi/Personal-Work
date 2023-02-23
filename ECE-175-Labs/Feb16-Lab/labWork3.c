#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
int main() {
    FILE* currFile = fopen("flights.txt", "r");
    long int val;
    long int total;
    long int minVal;
    char c;
    char flight[20];
    long int grandTotal = 0;
    long int negative = 1;
    int i = 0;
    c = fgetc(currFile);
    c = fgetc(currFile);
    int done = 0;
    printf("Enter the flight you want ");
    scanf("%s", flight);
    while(c != EOF) {
        if(c == 10) {
            int flag = 0;
            for (i = 0; i < strlen(flight); i++) {
                c = fgetc(currFile);
                if (c != flight[i]) {
                    flag = 1;
                }
            }
            if (flag != 1) {
                for(int i = 0; i<strlen(flight); i++) {
                    c = fgetc(currFile);
                }
                
                //printf("%c", c);
                if(c == 'L') {
                    printf("Flight has landed");
                } else if (c=='D') {
                    printf("Flight has departed");
                } else {
                    printf("Flight has been cancelled");
                }
                done = 1;
                return;
            } else {
                printf("not this one\n");
                done = 1;
            }
        }
        c = fgetc(currFile);
        fclose(currFile);
        if(done == 0) {
            currFile = fopen("flights.txt", "a");
            char input2;
            printf("write L for landed, D for departed, and C for cancelled\n");
            scanf("%*c%c", &input2);
            fprintf("%s %c\n", flight, input2);
            fclose(currFile);
        }
        


        
    }
    
    return;
}
