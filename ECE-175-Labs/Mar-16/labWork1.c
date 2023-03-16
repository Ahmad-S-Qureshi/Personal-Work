#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
void freq_num(int num, int counters[]){
    FILE* numbers = fopen("numbers.txt", "r");
    char currChar = fgetc(numbers);
    counters[num] = 0;
    while(currChar != EOF) {
        if(currChar == ('0' + num)) {
            counters[num]++;
        }
        currChar = fgetc(numbers);
    }
    fclose(numbers);
}
int main() {
    int counters[10];
    for (int i = 0; i< 10; i++) {
        freq_num(i, counters);
        if(counters[i] > 0) {
            printf("%d %d\n", i, counters[i]);
        }
    }

}
