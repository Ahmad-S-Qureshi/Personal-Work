#include <math.h>
#include <stdio.h>

char board[9][9];
int boardComplete[9];
int printBigBoard() {
    for(int i = 0; i <20; i++) {
        printf("\n");
    }
    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < 9; j++) {
            if(j%3==0 && j>0) {
                printf("| ");
            }
            printf("%c ", board[i][j]);
        }
        printf("\n");
        if(i%3 == 2 && i < 8) {
            printf("------+-------+-----\n");
        } 
    }
    
}
int main() {
    int players;
    printf("Welcome to ultimate tic-tac-toe\n");
    printf("For the purposes of this game, all boards will look like this:\n");
    printf("1 | 2 | 3\n4 | 5 | 6\n7 | 8 | 9\nInput any key to continue\n");
    scanf("%d", &players);
    printf("\n");
    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < 9; j++) {
            board[i][j] = ' ';
        }
    }
    char player = 'x';
    printf("Player %c, select what board you want to play in")
    while(1) {
        int end;
        char player = 'x';
        printBigBoard();

        printf("\n\nEnter 0 to continue and 1 to end: ");
        scanf("%d", &end);
        if(end == 1) {
            return 1;
        }
    }
}

