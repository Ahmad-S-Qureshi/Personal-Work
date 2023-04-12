#include <stdio.h>
#include<stdbool.h>
#define SIZE 9

void readSudoku(int x[][SIZE], FILE *inp);
void printSudoku(int x[][SIZE]);
bool checkSudoku(int x[][SIZE]);

int main(void){
    
    int sudoku[SIZE][SIZE]; // sudoku is a two dimensional array that holds all the values of the board
    FILE *inp;
    
    inp = fopen("sudoku1.txt", "r");
    
    if (inp == NULL){
        return -1;
    }
    else{
        readSudoku(sudoku, inp);
        printSudoku(sudoku);
        if(checkSudoku(sudoku)) {
            printf("This is a valid sudoku puzzle\n");
        } else {
            printf("This is not a valid sudoku puzzle\n");
        }
    }
}


void readSudoku(int x[][SIZE], FILE *inp) { // reads a sudoku file into array x
    int i = 0;
    int j = 0;
    int enters;
    char currChar = fgetc(inp);
    while(currChar != EOF) {
        if(currChar <= '9' && currChar >= '0') {
            x[j%SIZE][i%SIZE] = (currChar-'0');
            //printf("%d ",x[j%SIZE][i%SIZE]);
            i++;
        } else if (currChar == '\n' && enters%2 == 0) {
            //printf("\n");
            j++;
        }
        if(currChar == '\n') {
            enters++;
        }
        currChar = fgetc(inp);
    }

}

void printSudoku(int x[][SIZE]){ // prints a soduko board
    for(int row = 0; row<SIZE; row++) {
        for(int col = 0; col<SIZE; col++) {
            printf("%d ", x[row][col]);
            if(col%3 == 2 && col!=8) {
                printf("| ");
            }
        }
        printf("\n———————————\n");

    }
}

bool checkSudoku(int x[][SIZE]){ // returns true if x is a valid sudoku boards and false otherwise
    int output = 0;
    for(int rowBig = 0; rowBig<3; rowBig++) {
        for(int colBig= 0; colBig<3; colBig++) {
            for(int numCheck = 0; numCheck<10; numCheck++) {
               int gotten = 0;
                for(int row = 0; row<3; row++) {
                    for (int col = 0; col<3; col++) {
                        if(x[3*rowBig+row][3*colBig+col] == numCheck && gotten==0) {
                            output++;
                            gotten = 1;
                        }
                    }
                }
            }
            
        }
    }
    return output/81;
}





