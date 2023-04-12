#include <stdio.h>
#include <string.h>
#include <stdbool.h>
#define MAXLINE 1000
bool lineSearch(char s[], char target[]);


int main(void){
    char filepath[15];
    printf("Enter file path: ");
    scanf("%s%*c", filepath);
    char target[100];
    printf("Enter target: ");
    fgets(target, 100, stdin);
    int num = 0;
    FILE* fp = NULL;
    fp = fopen(filepath, "r");
    char text[100];
    if(fp == NULL) {
        printf("Still Nothing");
    }
    while(!feof(fp)) {
        fgets(text, 100, fp);
        num++;
        if(lineSearch(text, target)) {
            if(text[strlen(text)-1] == '\n')
                printf("%d %s", num, text);
            else {
                printf("%d %s", num, text);
                printf("\n");
            }
        }
    }
    printf("\n");
    return (0);
}

bool lineSearch(char s[], char target[]){
    int i = 0;
    int j = 0;
    while(i<strlen(s)) {
        j=0;
        while (s[i+j] == target[j] && j<strlen(target)){
            j++;
        }
        if(j==strlen(target)) {
            return true;
        }
        i++;
    }
    return false;
}
