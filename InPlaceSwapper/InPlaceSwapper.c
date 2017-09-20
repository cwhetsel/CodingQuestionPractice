/**
 *Question: Can you write a function to swap two numbers in place (without temporary variables)
 * Time To complete: 15 minutes 
 * 9/19/17
 * @author Christopher
 */

#include<stdio.h>
#include <stdlib.h>

int main(int argc, char** argv) {
    int len = 5;
    int arr[5] = {1, 2, 3, 4, 5};
    lprint(arr, len);

    printf("Swap 0, 4 \n");
    inPlaceSwap(arr, 0, 4, len);
    lprint(arr, len);

    printf("Swap 0, 2 \n");
    inPlaceSwap(arr, 0, 2, len);
    lprint(arr, len);

}
void inPlaceSwap(int* arr, int a, int b, int len) {
    if(arr == NULL) {
        return;
    }
    if(a > len || b > len || a < 0 || b<0) {
        return;
    }
    arr[a] = arr[a] + arr[b];
    arr[b] = arr[a] - arr[b];
    arr[a] = arr[a] - arr[b];
}

void lprint(int* arr, int len) {
    int i;
    for(i = 0; i < len; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}