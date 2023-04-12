#include <stdio.h>
#include <math.h>

void IntToReverseBinary(int integerValue, char* output, int* length) {
    int i = 0;
    while(integerValue>0) {
        output[i] = integerValue%2 + '0';
        integerValue /=2;
        i++;
    }
    output[i] = '\0';
    length = i-1;
}

long int StringReverse(char* input, long int output, int length) {
    for(int i = 0; i< length/2; i++) {
        char temp = input[i];
        
    }
}

int main(void) {
    char string[50];
    int m;
    IntToBinary(16, string);
    printf("%s", string);
    scanf("%d", &m);
    return 0;
}
