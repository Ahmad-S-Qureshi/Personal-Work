/* This program will display the pair of inputs that multiply to the third input*/

int main(void) {
    int num1;
    int num2;
    int num3;
    printf("\n Enter three numbers in the form 2 5 10, the program will then return a pair that multiplies to the third should one exist");
    scanf("%d %d %d", &num1, &num2, &num3);
    if(num1*num2 == num3) {
        printf("%d and %d multiply to %d", num1, num2, num3);
    } else if(num2*num3 == num1) {
        printf("%d and %d multiply to %d", num2, num3, num1);
    } else if(num1*num3 == num2) {
        printf("%d and %d multiply to %d", num1, num3, num2);
    } else {
        printf("There is no pair");
    }
}