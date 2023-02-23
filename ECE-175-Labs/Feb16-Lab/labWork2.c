#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
int SumInts(FILE *inp, int target) {
    long int val;
    long int total;
    int minVal = target;
    char c;
    long int grandTotal = 0;
    long int negative = 1;
    c = fgetc(inp);
    c = fgetc(inp);
    printf("Enter the minimum value ");
    while(c != EOF) {
    //for (int i = 0; i< 6; i++) {
        if(c<='9' && c>='0'){
            total *= 10;
            total += c-48;
        } else if(c == '-') {
            negative = -1;
        } else{
            if(total*negative >= minVal){
                grandTotal += total*negative;
                //printf("\n\n\n", c);
            }
            total = 0;
            negative = 1;
        }
        //printf("%c", c);
        c = fgetc(inp);
    }
    return grandTotal;
}
int main() {
    FILE* currFile = fopen("Thursdays_Data.dat", "r");
    long int minVal;
    scanf("%ld", &minVal);
    printf("\nThe sum of all values >= %d was found to be %ld", minVal, SumInts(currFile, minVal));
}
