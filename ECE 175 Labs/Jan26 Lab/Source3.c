#include <stdio.h>
#include <math.h>

int main(void) {
	int numberBig;
	int numberSmall;
	float price;
	printf("Enter the number of big and small bottles you would like: ");
	scanf("%d %d", &numberSmall, &numberBig);
	price = numberBig*0.02 + numberSmall*0.008;
	//printf("\n\n %f  %f    %f %d     \n\n", price, numberSmall*0.008, numberBig*0.02, numberSmall + numberBig);
	if(price < 200.0) {
		price = price;
	} 
	if (price > 200.0 || ((numberBig + numberSmall) > 3000)) {
		price = price * 0.94;
	} 
	if (price > 600) {
		price = price * 0.8;
	}
	//printf("\n\n %f \n\n", price);

	printf("\n The total price of %d small bottles and %d big bottles is $%.2f\n", numberSmall, numberBig, price);
}