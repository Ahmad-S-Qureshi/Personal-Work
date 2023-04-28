#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>

typedef struct {
  char Name[20];
  double TotalArea;
  double WaterArea;
  double LandArea;
  int Population;
  int Rank;
} State;

void scanState(State *x, FILE *in) {
    fscanf(in, "%d %s %d %lf %lf", &(x->Rank), x->Name,&(x->Population), &(x->TotalArea), &(x->WaterArea));
    x->LandArea = x->TotalArea-x->WaterArea;
}

void printState(State *x) {
    printf("%d %s %d %lf %lf\n", x->Rank, x->Name, x->Population, x->TotalArea, x->WaterArea);
}

void selectionState(State x[], int size) {
  // selection sort
  int i, j;
  int min;
  State temp;

  for (i = 0; i < size; i++)
  {
    min = i; // start searching from currently unsorted
    for (j = i; j < size; j++)
    {
      if (x[j].LandArea > x[min].LandArea) // if found a smaller element
        min = j; // move it to the front
    }
    temp = x[i];
    x[i] = x[min];
    x[min] = temp;
  }
}


void sortState(State x[], int size) {
    selectionState(x, size);
}


int main(){
    FILE *fp = fopen("StateData.txt", "r");
    State states[10];
    int i = 0;
    while(!feof(fp)) {
        scanState(&states[i], fp);
        i++;
    }
    sortState(states, 10);
    for(int i = 0; i<10; i++) {
      printState(&states[i]);
    }

}