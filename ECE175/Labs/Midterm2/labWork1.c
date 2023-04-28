#include <stdio.h>
#include <math.h>
#include <string.h>
#include <limits.h>
#include <stdlib.h>

//Functions were left unchanged to use ints despite what was specified below
//The prompts reads as below:
//read the file data into a float array named “data”.
//This was chosen to keep functions the same since functions were consistently using ints and not floats

//This code displays the sorted as well as unsorted due to uncertainty in the prompt
//The prompt reads: Display the entire sorted array and the index of the target.
//Though the test cases print: DataInput.txt: 35 22 66 88 55 -20 122

void selectionSort(int data[], int size) {
    int i, j, minIndex;
    int tmp;
        for (i = 0; i < size-1; i++) {
        minIndex = i;
            for (j = i+1; j < size; j++) {
                if (data[j] < data[minIndex]) {
                    minIndex = j;
                }
            }
            if (minIndex != i) {
                tmp = data[i];
                data[i] = data[minIndex];
                data[minIndex] = tmp;
            }
        }
}

int binarySearch(int data[], int size, float target, int *iterations) {
    int leftEnd = 0;
    int rightEnd = size;
    int middle = size/2;
    *iterations=1;
    while(data[middle] != target && rightEnd != leftEnd) {
        (*iterations)++;
        if(data[middle] > target) {
            int tempMiddle = middle;
            rightEnd = middle;
            middle = (rightEnd+leftEnd)/2;
            if(middle == tempMiddle) {
                leftEnd = rightEnd;
            }
        } else if (data[middle] < target){
            int tempMiddle = middle;
            leftEnd = middle;
            middle = (rightEnd+leftEnd)/2;
            if(middle == tempMiddle) {
                leftEnd = rightEnd;
            }
        } else {
            break;
        }
    }
    if(leftEnd == rightEnd) {
        return -1;
    }
    return middle + 1;
}

int readFile (int data[], int size, FILE *inp) {
    int currNum = 0;
    while(!feof(inp)) {
        fscanf(inp, "%d", &data[currNum]);
        printf("%d ", data[currNum]);
        currNum++;
    }
    return currNum;
}

int main(){
    char filename[50];
    printf("Enter the name of the data file: ");
    scanf("%s", filename);
    FILE *fp = fopen(filename, "r");
    int nums[20];
    printf("%s's file contents are: ", filename);
    int currNum = readFile(nums, 20, fp);
    printf("\n");
    selectionSort(nums, currNum);
    printf("%s's file contents sorted are: ", filename);
    for(int i = 0; i<currNum; i++) {
        printf("%d ", nums[i]);
    }
    int target;
    int iterations;
    printf("\nEnter the target value: ");
    scanf("%d", &target);
    int index = binarySearch(nums, currNum, target, &iterations);
    if(index > 0) {
        printf("Number %d was found at location %d of the sorted array in %d comparisons.\n", target, index, iterations + 1);
    } else {
        printf("Number %d was not found.\n", target);
    }
}