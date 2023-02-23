#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
int oblong(int total) {
    return ((int)(sqrt(total)) * ((int)(sqrt(total))+1) == total);
}
int main() {
    FILE* currFile = fopen("numbers.txt", "r");
    int val;
    int total;
    char c;
    c = fgetc(currFile);
    printf("The set of oblong numbers is ");
    while(c != EOF) {
        if(c !=' '){
            total *= 10;
            total += c-48;
        } else {
            if(isOblong(total)){
                printf("%d  ", total);
            }
            total = 0;
        }
        c = fgetc(currFile);
    }
    
}
