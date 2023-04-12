#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>

int main() {
    //printf("got here");
    char currWord[100];
    char reverseWord[100];
    FILE *inputfp = fopen("Palindrome_Input.txt", "r");
    FILE *outputfp = fopen("palindromes.txt", "w");

    while(!feof(inputfp)) {
        fgets(currWord, 100, inputfp);
        int lenCurrWord = strlen(currWord);
        int lenEqual = 1;
        for(int i = 0; i<lenCurrWord; i++) {
            if(currWord[i-1] == currWord[lenCurrWord - 2- i]) {
                lenEqual++;
                //printf("%s equal for %d out of%d with letter %c and %c\n", currWord, lenEqual, lenCurrWord, currWord[i-1], currWord[lenCurrWord - 2-i]);
            } else {(currWord, 100, inputfp);
                //printf("%s not equal for %d out of%d with letter %c and %c\n", currWord, lenEqual, lenCurrWord, currWord[i-1], currWord[lenCurrWord - 2-i]);
            }
        }
        if(lenEqual == strlen(currWord)-1) {

            fprintf(outputfp,"%s", currWord);
            lenEqual=0;
        }
    }
}
