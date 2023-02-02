#include<stdio.h>
#include<stdbool.h>
#include<math.h>

#define IDEAL_AWAKE 21.2 // Ideal daytime temperature
#define IDEAL_SLEEP 18.3 // ideal nightime temperature

int main(void){
    
    float currentTemp; // temperature entered by user
    char userTime; // time of the day entered by user
    bool timeOfDay; // boolean var that holds if it is daytime (true) or nighttime (false)
    
    printf("Day (d) or Night (n): ");
    scanf("%c", &userTime);
    printf("%c", userTime);
    if (userTime == 'n') {
      timeOfDay = false;
    } else if (userTime == 'd') {
      timeOfDay = true;
    } else {
      printf("Invalid Input");
    }
    printf("Enter the current temperature: ");
    scanf("%f", &currentTemp);
    if(timeOfDay) {
      if(21.2-currentTemp > 0.01) {
         printf("You need to raise the temperature by %f", 21.2-currentTemp);
      } else if (21.2-currentTemp < 0.01) {
         printf("You need to lower the temperature by %f", 21.2-currentTemp);
      } else {
         printf("The temperature is ideal");
      }
    } else {
      if(18.3-currentTemp > 0.01) {
         printf("You need to raise the temperature by %f", 18.3-currentTemp);
      } else if (18.3-currentTemp < 0.01) {
         printf("You need to lower the temperature by %f", 18.3-currentTemp);
      } else {
         printf("The temperature is ideal");
      }
    }
    return 0;
    
}
