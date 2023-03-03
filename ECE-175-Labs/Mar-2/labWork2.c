#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
int main() {
    char input;
    printf("Which character would you like to find?");
    scanf("%c", &input);
    char currChar;
    int charOnLine = 0;
    int line = 1;
    FILE* inputFile = fopen("inputFile.txt", "r");
    while(currChar != EOF) {
        currChar = fgetc(inputFile);
        if(currChar == input) {
            charOnLine++;
        } else if (currChar == '\n') {
            printf("Character %c was found %d times in line %d\n", input, charOnLine, line);
            charOnLine = 0;
            line++;
        }

    }

}
