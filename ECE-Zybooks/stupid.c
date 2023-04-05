//modify (04/03/2019) by Kay to get the correct value of mean

#include <stdio.h>
#include<math.h>
#include<string.h>

typedef struct{
    double mantissa;
    int exponent;
} sciNotation;

sciNotation convert(double num); // converts a double to scientific notation
sciNotation meanVal(sciNotation arr[], int len); // computes the mean value of the array and returns mean in scientific notation
void printVal(sciNotation *num); // prints a number in scientific notation

int main(void){
   sciNotation enteredVals[10];
   printf("Enter a value: ");
   float input;
   scanf("%f", &input);
   sciNotation converted;
   converted = convert(input);
   printVal(&converted);
   char letterIn = 'y';
   printf("\nDo you want to enter another value (y/n)? ");
   scanf("%*c%c", &letterIn);
   int currPos = 0;
   enteredVals[currPos] = converted;
   //printf("%f ", input);
   while (letterIn != 'n' && (currPos +1 < 10)) {
      printf("\nEnter a value: ");
      scanf("%f", &input);
      converted = convert(input);
      printVal(&converted);
      printf("\nDo you want to enter another value (y/n)? ");
      scanf("%*c%c", &letterIn);
      currPos++;
      enteredVals[currPos] = converted;
   }
   sciNotation meanTot = meanVal(enteredVals, currPos+1);
   printf("\nMean Value: ");
   printVal(&meanTot);
   printf("\n");
   return 0;
}

sciNotation convert(double num){
   if(num<0.0000001 && num > -0.0000001) {
      sciNotation output;
      output.mantissa = 0;
      output.exponent = 0;
      return output;
   }
   int negative = 1;
   int exponent = 0;
   if(num<0) {
      negative = -1;
      num*=negative;
   }
   if(num<1){
      while(num<1) {
         exponent++;
         num*=10;
      }
   } else if (num>1) {
      while(num>1) {
         exponent--;
         num/=10;
      }
      exponent++;
      num*=10;
   }
   sciNotation output;
   output.exponent = exponent*-1;
   output.mantissa = negative*num;
   return output;
    
}

sciNotation meanVal(sciNotation arr[], int len){
   float sum = 0.0;
   for(int i = 0; i<len; i++) {
      sum += (arr[i].mantissa) * pow(10, arr[i].exponent);
   }
   sum/=len;
   return (convert(sum));
   // mean computation function
      
}


void printVal(sciNotation *num){
   double mantissa = num->mantissa;
   if(mantissa < 0) {
      mantissa*=-1;
      printf("-");
   }
   printf("%d.", (int)(mantissa));
   mantissa-=(int)(mantissa);
   mantissa *=10;
   if(mantissa>= 0.00001) {
   while(mantissa>= 0.00001) {
      if(mantissa - (int)(mantissa) > 0.9999) {
         printf("%d", (int)(mantissa)+1);
         break;
      }
      printf("%d", (int)(mantissa));
      mantissa-=(int)(mantissa);
      mantissa*=10;
   }
   } else {
    printf("0");
   }
   if(num->exponent > 0) {
      printf("E+%d", num->exponent);
   }else{
      printf("E%d", num->exponent);
   }
   
   
    
}
