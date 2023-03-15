#include <math.h>
#include <stdio.h>

void initBoard(char board[][3][3][3]) {
   // initialize all elements to space character
   for(int i=0; i<3; i++) {
      for(int j=0; j<3; j++) {
         for(int k=0; k<3; k++) {
            for(int l=0; l<3; l++) {
               board[i][j][k][l] = ' ';
            }
         }
      }
   }
}

void displayBoard(char board[][3][3][3]) {
   printf("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n");
   int loopOuter = 0;
   int loopInner = 0;
   int currChar = 0;
   for(int i=0; i<3; i++) {
      for(int j=0; j<3; j++) {
         for(int k=0; k<3; k++) {
            for(int l=0; l<3; l++) {
               if(currChar%3 == 0 && currChar>0) {
                printf("| ");
               }
               currChar++;
               printf("%c ", board[i][k][j][l]);
            }
            if(loopInner%3==2) {
                printf("\n");
                currChar = 0;
            }
            loopInner++;
         }
        if(loopOuter%3 ==2) {
            //printf("\n");
            if(loopOuter<7) {
                printf("------+-------+------\n");
            }

        }
        loopOuter++;
      }
   }
}

int main() {
   char board[3][3][3][3];

   // initialize the array using the initBoard function
   initBoard(board);

   // print the array and start the game
   int inputBoard;
   int inputSquare;
   char player = 'X';
    while(1) {
        displayBoard(board);
        printf("\nSelect which board you want to do your turn in using the following pattern of a board (0 to end)\n1|2|3\n4|5|6\n7|8|9\n");
        scanf("%d", &inputBoard);
        if(inputBoard == 0) {
            return 0;
        }
        printf("\nSelect which square you want to do your turn in using the following pattern of a board \n1|2|3\n4|5|6\n7|8|9\n");
        scanf("%d", &inputSquare);
        board[(inputBoard-1)/3][(inputBoard-1)%3][(inputSquare-1)/3][(inputSquare-1)%3] = player;
        if(player=='X') {
         player = 'O';
        } else {
         player = 'X';
        }
    }
}

