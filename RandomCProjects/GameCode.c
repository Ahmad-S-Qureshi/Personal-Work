#include <math.h>
#include <stdio.h>

char board[9][9];
int printBoard() {
    for(int i = 0; i <20; i++) {
        printf("\n");
    }
    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < 9; j++) {
            if(j%3==0 && j>0) {
                printf("||| ");
            }
            printf("%c |", board[i][j]);
        }
        printf("\n");
        if(i%3 == 2 && i < 8) {
            printf("--------------------------\n---------------------------\n---------------------------\n");
        } else {
            printf("--------------------------\n");
        }
    }
    
}
int main() {
    int players;
    printf("Welcome to ultimate tic-tac-toe\nEnter number of players: ");
    scanf("%d", &players);
    printf("\n");
    for(int i = 0; i < 9; i++) {
        for(int j = 0; j < 9; j++) {
            board[i][j] = ' ';
        }
    }

    while(1) {
        int end;

        printBoard();

        printf("\n\nEnter 0 to play again and 1 to end: ");
        scanf("%d", &end);
        if(end == 1) {
            return 1;
        }
    }
}

