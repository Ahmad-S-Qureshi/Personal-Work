#include <stdio.h>
#include <math.h>

int main(void) {
	int weight;
	float height;
	printf("Enter your weight in kilos: ");
	scanf("%d", &weight);
	printf("\nEnter your height in meters: ");
	scanf("%f", &height);
	int BMI = weight / ((pow(height, 2.0)));
	if (BMI < 20) {
		printf("You have below normal weight\n");
	} else if (BMI < 25) {
		printf("You are normal weight\n");
	} else if (BMI < 30) {
		printf("You are overweight\n");
	} else {
		printf("You are obese\n");
	}

	return;
}