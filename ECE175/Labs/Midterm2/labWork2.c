#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>
#include <stdbool.h>

typedef struct {
    char name[100];
    int studentID;
    float gpa;
} student;

bool gpaSearch (student pt, float targetGpa) {
    if(pt.gpa > targetGpa) {
        return true;
    } else {
        return false;
    }
}

int readEntry (student roster[], int size, int *index) {
    printf("Enter the student title: ");
    char title[100];
    scanf("%s", title);
    printf("Enter the student ID: ");
    int ID;
    scanf("%d", &ID);
    printf("Enter the student GPA: ");
    float gpa;
    scanf("%f", &gpa);
    student toBeAdded;
    toBeAdded.gpa = gpa;
    toBeAdded.studentID=ID;
    strcpy(toBeAdded.name, title);
    roster[*index] = toBeAdded;
    (*index)++;
    int returnVal = size+1;
    return returnVal;
}

int main(){
    student roster[10];
    char input;
    int index = 0;
    int size = 0;
    printf("Press y to enter a new student into the database or q to quit: ");
    scanf("%c%*c", &input);
    while (input == 'y') {
        size=readEntry(roster, size, &index);
        printf("Press y to enter a new student into the database or q to quit: ");
        scanf("%*c%c", &input);
        if(size>=10) {
            printf("The database is full, you cannot add any more students to the roster\n");
            input='q';
        }
    }
    float target;
    printf("Search the student database by GPA: ");
    scanf("%f", &target);
    printf("The following students were found:\n\n");
    for(int i = 0; i<size; i++) {
        if(gpaSearch(roster[i], target)) {
            printf("Name:%s\nStudent ID: %d\nGPA:%G\n\n", roster[i].name, roster[i].studentID, roster[i].gpa);
        }
    }

    
}