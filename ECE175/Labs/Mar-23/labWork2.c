#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>


void printBoard(int x[][3]) {
    for(int i = 0; i<3; i++) {
        for(int j=0; j<3; j++) {
            printf("%c|", x[i][j]);
        }
        printf("\n");
    }
}

int checkBoard(int x[][3]) {
        if((x[0][0] == x[0][1] && x[0][1]== x[0][2] && x[0][0] != ' ') ||
            (x[1][0] == x[1][1] && x[1][2] == x[1][1] && x[1][0] != ' ') ||
            (x[2][0] == x[2][1] && x[2][2] == x[2][1] && x[2][0] != ' ') ||
            (x[0][0] == x[1][0] && x[2][0]== x[1][0] && x[0][0]!= ' ') ||
            (x[0][1] == x[1][1] && x[2][1]== x[1][0]&& x[0][1]!= ' ')||
            (x[0][2] == x[1][2] && x[2][2]== x[1][0]&& x[0][2]!= ' ')||
            (x[0][0] == x[1][1] && x[2][2]== x[1][1]&& x[0][0]!= ' ')||
            (x[0][2] == x[1][1] && x[2][0]== x[1][1]&& x[0][2]!= ' ' )
        ) {
            return 'd';
        } else {
            return 'n';
        }
    }

int main() {
    char input;
    char player = 'x';
    int xpos;
    int ypos;
    //scanf("%c", &input);
    int board[3][3];
    for(int i = 0; i<3; i++) {
        for(int j=0; j<3; j++) {
            board[i][j] = ' ';
        }
    }
    
    while(input != 'q' && checkBoard(board) == 'n'){
        printBoard(board);
        printf("%c's turn\n", player);
        printf("Enter your x and y pos like this \"3 3\": ");
        scanf("%d %d%*c", &xpos, &ypos);
        xpos--;
        ypos--;
        board[xpos][ypos] = player;
        printf("\nPress q to quit: ");
        scanf("%c", &input);
        int done = 0;
        for(int i=0; i<3; i++) {
            
            for(int j=0; j<3; j++) {
                
                if(board[i][j] == ' ' && done != 1) {
                    board[i][j] = 'o';
                    done = 1;
                }
            }
        }
    }
    printBoard(board);


}
