#include <stdio.h>
#include <string.h>
#include <time.h>
#include <unistd.h>

int main() {
    char word[100];
    strcpy(word, "test word");
    for(int i = 0; i<strlen(word); i++) {
        printf("%c", word[i]);
        sleep(1);
        fflush(stdout);
        
    }
    printf("\n");
}