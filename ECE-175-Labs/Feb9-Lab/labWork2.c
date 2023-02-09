#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
int main() {
    FILE* currFile = fopen("Thursdays_Data.dat", "r");
    long int val;
    long int total;
    long int minVal;
    char c;
    long int grandTotal = 0;
    long int negative = 1;
    c = fgetc(currFile);
    
    c = fgetc(currFile);
    printf("Enter the minimum value ");
    scanf("%ld", &minVal);
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
            }
            total = 0;
            negative = 1;
        }

        c = fgetc(currFile);
    }
    printf("\nThe sum of all values >= %d was found to be %ld", minVal, grandTotal);
}
