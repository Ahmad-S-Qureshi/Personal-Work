#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>

typedef struct {
        char brand [20];
        float mpg ;
        int power ;
        double msrp ;
} car_t;

car_t *scanCar(FILE *inp, int *numCars_pt);
void printCar(car_t x);
int main(){
    FILE* fp = fopen("cars.txt", "r");
    int length = 0;
    fscanf(fp,"%d", &length);
    //printf("%d\n", length);
    car_t* cars = scanCar(fp, &length);
    // for(int i = 0; i<length; i++) {
    //     printf("%lf\n", cars->mpg);
    // }
     for(int i = 0; i<length; i++) {
         printCar(cars[i]);
    }

}

car_t *scanCar(FILE *inp, int *numCars_pt) {
    car_t *carPtr = NULL;
    carPtr = (car_t*)malloc((*numCars_pt)*sizeof(car_t));
    for(int i = 0; i<*numCars_pt; i++) {
        fscanf(inp, "%s %f %d %lf", &carPtr[i].brand, &carPtr[i].mpg, &carPtr[i].power, &carPtr[i].msrp);
    }
    return carPtr;
}


void printCar(car_t x) {
    printf("%s\t%.1lf\t%d\t%.0lf\n", x.brand, x.mpg, x.power, x.msrp);
}
