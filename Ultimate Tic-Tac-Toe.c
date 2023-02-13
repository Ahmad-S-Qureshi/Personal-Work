#include <stdio.h>

int initializeBoardRow(char (*boardCurrRow)[9]) {
    for (int i = 0; i < 9; i++) {   
        (*boardCurrRow)[i] = ' ';
    }
}
int initializeBoard(char (*board)[9][9]) {
    for(int i = 0; i < 9; i++) {
        initializeBoardRow(&(*board)[i]);
    }
}

int main(void) {
    char board[9][9]; 
    char grids[3][3];
    char currGrid[3][3];
    int prevBoard;
    char currPlayer = 'x';
    initializeBoard(&board);
    for (int i = 0; i<9; i++) {
        for(int j = 0; j < 9; j++) {
            if(j != 8 && j%3 == 2) {
                printf("%c | ", board[i][j]);
            } else {
                printf("%c ", board[i][j]);
            }
        }
        if(i%3 == 2 && i!=8) {
            printf("\n------+");
            printf("-------+");
            printf("------");            
        }
        printf("\n");
    }
    printf("In this game, all charts are laid out as such\n1 | 2 | 3\n--+---+--\n4 | 5 | 6\n--+---+--\n7 | 8 | 9\n");
    printf("x select the first grid: ");
    scanf("%d", &prevBoard);
    
    //while(!won(&currGrid)) {

    //}
        
}
