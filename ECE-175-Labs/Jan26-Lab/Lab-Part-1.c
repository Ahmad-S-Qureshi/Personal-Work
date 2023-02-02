#include <stdio.h>
#include <math.h>

int main(void) {
	int weight;
	float height;
	printf("Enter your weight in kilos: ");
	scanf_s("%d", &weight);
	printf("\nEnter your height in meters: ");
	scanf_s("%d", &height);
	int BMI = weight/((pow(height, 2.0)))
	if (BMI < 20) {
		printf("You have below normal weight");
	} else if {
		printf("You are normal weight");
	} else if (BMI < 30) {
		printf("You are overweight");
	} else {
		printf("You are obese")
	}

	return;
}