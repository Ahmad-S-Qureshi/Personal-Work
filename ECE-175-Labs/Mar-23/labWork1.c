#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
void fingerLoc(int screen[][10], int *x_p, int *y_p) {
    int max = 0;
    int count =0;
    int currVal = 0;
    for(int col = 1; col<=8; col++) {
        for(int row = 1; row<=7; row++) {
            for(int currCol= col-1;currCol<=col+1; currCol++) {
                for(int currRow = row-1; currRow <= row + 1; currRow++) {
                    currVal+=screen[currRow][currCol];
                    count++;
                }
            }
            //printf("%d ", currVal);
            if(currVal>max) {
                max = currVal;
                *x_p = row+3;
                *y_p = col+3;
                //printf("\n\n\n\n%d %d %d\n\n\n", row, col, 1);
            }
            currVal=0;
            count = 0;
        }
    }
}

int main() {
    int screen[9][10];
    FILE* fp = fopen("pressure.txt", "r");
    char currChar = fgetc(fp);
    int row = 0;
    int col = 0;
    while(currChar != EOF) {
        if(currChar >= '0' && currChar<='9') {
            screen[row][col] = currChar-'0';
            col++;
            //printf("%d ", currChar-'0');
        }
        if(currChar == '\n') {
            row++;
            //printf("\n");
        }
        currChar = fgetc(fp);
    }
    int xpos;
    int ypos;
    fingerLoc(screen, &xpos, &ypos);
    printf("The finger location is at (%d, %d) coordinate.\ns", xpos, ypos);
}
