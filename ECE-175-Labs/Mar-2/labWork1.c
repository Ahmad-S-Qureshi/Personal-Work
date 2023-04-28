#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
void daysFwd(int n, int day, int month, int year){
    
    int totalDays1 = (day) + (month-1)*30 + year*360 + n;
    int totalDays = totalDays1;
    //printf("totalDays = %d\n", totalDays);
    year = (totalDays/360);
    totalDays = totalDays - 360*year;
    month = (totalDays/30);
    totalDays = totalDays - 30*month;
    day = totalDays + 1;
    month++;
    totalDays = month*30 + day + year*360;
    if(totalDays%7 == 0) {
        printf("\nYour %d-th birthday is on Sunday, %d/%d/%d.", n, month, day, year);
    } else if (totalDays%7 == 1) {
        printf("\nYour %d-th birthday is on Monday, %d/%d/%d.", n, month, day, year);
    } else if (totalDays%7 == 2) {
        printf("\nYour %d-th birthday is on Tuesday, %d/%d/%d.", n, month, day, year);
    } else if (totalDays%7 == 3) {
        printf("\nYour %d-th birthday is on Wednesday, %d/%d/%d.", n, month, day, year);
    } else if (totalDays%7 == 4) {
        printf("\nYour %d-th birthday is on Thursday, %d/%d/%d.", n, month, day, year);
    } else if (totalDays%7 == 5) {
        printf("\nYour %d-th birthday is on Friday, %d/%d/%d.", n, month, day, year);
    } else if (totalDays%7 == 6) {
        printf("\nYour %d-th birthday is on Saturday, %d/%d/%d.", n, month, day, year);
    }
    printf("\n");
} 

int main() {
    int day;
    int month;
    int year;
    int daysForward;
    printf("Enter your date of birth(mm dd year):");
    scanf("%d %d %d ", &month, &day, &year);
    printf("\nEnter the number of days forward:");
    scanf("%d", &daysForward);
    daysFwd(daysForward, day, month, year);
}
