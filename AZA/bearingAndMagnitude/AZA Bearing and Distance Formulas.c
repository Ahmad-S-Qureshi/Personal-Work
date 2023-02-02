#include <stdio.h>
#include <math.h>

float calcBearing(int xpos, int ypos, int xmax, int ymax) {
    float radians;
    xpos = xmax-xpos;
    // Validate input values
    if (xmax <= 0 || ymax <= 0) {
        printf("Error: xmax and ymax must be positive values.\n");
        return NAN;
    }
    if (xpos < 0 || xpos > xmax || ypos < 0 || ypos > ymax) {
        printf("Error: (xpos, ypos) must be within the range of (0, 0) to (xmax, ymax).\n");
        return NAN;
    }

    if(xpos > xmax/2 && ypos < ymax/2) {
        radians = atan((float)(xpos - xmax/2)/(ymax/2 - ypos));
        radians = radians + 3.1415926/2;
    } else if (xpos > xmax/2 && ypos > ymax/2){
        radians = atan((float)(ypos - ymax/2)/(xpos-xmax/2));
        radians = radians + 3.1415926;
    } else if (xpos < xmax/2 && ypos > ymax/2){
        radians = atan((float)(xmax/2 - xpos)/(ypos - ymax/2));
        radians = radians + 3*3.1415926/2;
    } else {
        radians = atan((float)(ymax/2 - ypos)/(xmax/2 - xpos));
    }
    return radians * 180 / 3.1415926;
}

float calcMagnitude(int xpos, int ypos, int xmax, int ymax, float height, float maxDegrees) {
    xpos = xmax-xpos;
    if (xmax <= 0 || ymax <= 0) {
        printf("Error: xmax and ymax must be greater than 0\n");
        return -1;
    }
    if (maxDegrees < 0 || maxDegrees >= 90) {
        printf("Error: maxDegrees must be between 0 and 90 degrees\n");
        return -1;
    }
    if (xpos < 0 || xpos > xmax) {
        printf("Error: xpos and ypos must be between 0 and xmax, ymax respectively\n");
        return -1;
    }
    float feet;
    float maxFeet = height*tan(maxDegrees/180*3.1415926);
    float xDistPixels = xpos-xmax/2;
    float yDistPixels = ypos-ymax/2;
    float pixelsFromCornertoMiddle = (pow(pow(xmax/2, 2) + pow(ymax/2, 2), 1.0/2));
    float feetPerPixel = maxFeet/pixelsFromCornertoMiddle;
    if(xpos != 0){
        float totalDistPixels = pow(pow(xDistPixels, 2) + pow(yDistPixels, 2), 0.5);
        //printf("ratio = %.2f ", totalDistPixels/pixelsFromCornertoMiddle);
        feet = totalDistPixels * feetPerPixel;
    }else{
        feet = yDistPixels * feetPerPixel;
    }
    return fabs(feet);
}


int main(void){
    
    FILE* file = fopen("output1.csv", "w");
    if (file == NULL) {
        printf("Error opening file!\n");
        return 1;
    }
    fprintf(file, "x, y, feet, theta\n");
    for(int i = 0; i < 3000; i = i+10){
        for(int j = 0; j < 4000; j = j+10) {
            fprintf(file, "%d,  %d, %.2f, %.2f\n", i, j, calcMagnitude(i, j, 3000, 4000, 50, 10.7), calcBearing(i, j, 3000, 4000));
        }
    }
    fclose(file);

    printf("Text written to file successfully.\n");
    return 0;
    
}