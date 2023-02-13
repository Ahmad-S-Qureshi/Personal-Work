#include <stdio.h>

void CoordTransform(int xIn, int yIn, int* xOut, int* yOut) {
   yOut = (yIn+1)*2;
   xOut = (xIn+1)*2;
}

int main(void) {
   int xValNew;
   int yValNew;
   int xValUser;
   int yValUser;

   scanf("%d", &xValUser);
   scanf("%d", &yValUser);

   CoordTransform(xValUser, yValUser, &xValNew, &yValNew);
   printf("(%d, %d) becomes (%d, %d)\n", xValUser, yValUser, xValNew, yValNew);

   return 0;
}