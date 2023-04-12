#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
void calculateTrialRating(int Data[][3], double Rating[], char difficulty[][15]) {
    for(int i =0; i<10; i++) {
        double changeInHeight = fabs(Data[i][1] - Data[i][2]);
        printf("%d\t%d\t%.2f\n", Data[i][1], Data[i][2], fabs(Data[i][1] - Data[i][2]));
        Rating[i] = 100*sqrt(changeInHeight*changeInHeight/(Data[i][1]*Data[i][0]));
        if(Rating[i] > 28) {
            strcpy(difficulty[i], "Extreme");
        } else if (Rating[i] >= 24) {
            strcpy(difficulty[i], "Very Difficult");
        }else if (Rating[i] >= 19) {
            strcpy(difficulty[i], "Difficult");
        }else if (Rating[i] >= 14) {
            strcpy(difficulty[i], "Challenging");
        }else if (Rating[i] >= 8) {
            strcpy(difficulty[i], "Moderate");
        } else {
            strcpy(difficulty[i], "Easy");
        }
    }
}
int main() {
    FILE *inputfp = fopen("Hiking_Trail_Data.txt", "r");
    FILE *outputfp = fopen("data.txt", "w");
    char currWord[100];
    char name[50];
    int heightMin=0;
    int heightMax=0;
    int distance=0;
    char Names[50][15];
    int Data[10][3];
    int j = 0;
    while(j<10) {
        fgets(currWord, 100, inputfp);
        int lenCurrWord = strlen(currWord);
        //printf("%s", currWord);
        int i = 0;
        while(currWord[i] != ' ' && currWord[i] != '\0') {
            name[i] = currWord[i];
            i++;
        }
        while(currWord[i] == ' '&& currWord[i] != '\0'){
            i++;
        }
        while (currWord[i] == '0'||currWord[i] == '1'||currWord[i] == '2'||currWord[i] == '3'||currWord[i] == '4'||currWord[i] == '5'||currWord[i] == '6'||currWord[i] == '7'||currWord[i] == '8'||currWord[i] == '9'){
            distance*=10;
            //printf("currHeight = %d", height);
            distance+=currWord[i]-'0';
            i++;
        }
        while(currWord[i] == ' '&& currWord[i] != '\0'){
            i++;
        }
        while (currWord[i] == '0'||currWord[i] == '1'||currWord[i] == '2'||currWord[i] == '3'||currWord[i] == '4'||currWord[i] == '5'||currWord[i] == '6'||currWord[i] == '7'||currWord[i] == '8'||currWord[i] == '9'){
            heightMin*=10;
            //printf("currHeight = %d", height);
            heightMin+=currWord[i]-'0';
            i++;
        }
        while(currWord[i] == ' '&& currWord[i] != '\0'){
            i++;
        }
        while (currWord[i] == '0'||currWord[i] == '1'||currWord[i] == '2'||currWord[i] == '3'||currWord[i] == '4'||currWord[i] == '5'||currWord[i] == '6'||currWord[i] == '7'||currWord[i] == '8'||currWord[i] == '9'){
            heightMax*=10;
            //printf("currHeight = %d", height);
            heightMax+=currWord[i]-'0';
            i++;
        }
        name[i] = '\0';
        //printf("%s %d %d %d\n", name, distance, heightMin, heightMax);
        strcpy(Names[j], name);
        Data[j][0] = distance;
        Data[j][1] = heightMin;
        Data[j][2] = heightMax;
        heightMin = 0;
        heightMax = 0;
        distance = 0;
        j++;
        
    }
    double Rating[10];
    char Difficulties[10][15];
    calculateTrialRating(Data, Rating, Difficulties);
    for(int i = 0; i<10; i++) {
        //printf("%s\t%d\t%d\t%d\n", Names[i], Data[i][0],Data[i][1],Data[i][2]);
        fprintf(outputfp, "%s\t%.2f\t%s\n", Names[i], Rating[i],Difficulties[i]);
    }
}
