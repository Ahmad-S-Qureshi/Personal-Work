#include <stdio.h>
#define MAX 1000

int main() {
   int bins[MAX];
   for (int i = 0; i<1000; i++) {
        bins[i] = 0;
   }
   for (int i=1; i<100; i++) {
      for(int j = 0; j<MAX; j += i) {
         if(bins[j] == 0) {
            bins[j] = 1;
         } else {
            bins[j] = 0;
         }
      }
   }
   int count = 0;
   for(int i = 0; i<1000; i++) {
      if(bins[i] == 0) {
         count++;
      }
   }
   printf("Number of empty bins: %d", count);
   return 0;
}
