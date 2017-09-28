/*
    Question: Given two integer arrays, compute the pair of values(one from each array) with the smallest nonnegative difference. Return the difference
    9/25/17
    Time: 30 min 
    A brute force method would be to have a nested loop which calculates the difference of each possible pair and returns the smallest nonnegative. 
    This would run in O(n*l) where is the length of the first list and l is length of the second list. However, we can improve the performance by 
    sorting the arrays first. 
*/

#include<stdio.h>
#include<stdlib.h>

int findSmallestDifferencePair(int*, int*, int*);
int cmpfunc (const void * a, const void * b);

int main(int argc, char** argv) {
    int* pair = malloc(sizeof(int)*2);
    int list1[6] = {1, 3, 15, 11, 2, 5};
    int list2[6] = {23, 127, 14, 19, 6, 10};
    int size1 = 6, size2 = 6;
    int diff = findSmallestDifferencePair(list1, list2, size1, size2, &pair);
    printf("(%d, %d) has difference %d ", pair[0], pair[1], diff );
    

    return (EXIT_SUCCESS);
}

int findSmallestDifferencePair(int* list1, int* list2, int size1, int size2, int** pair) {
    if(list1 == NULL || list2 == NULL) {
        return -1;
    }
    else {
        //we can sort the input so we only have to deal with the pairs we know will not have a negative difference
        qsort(list1, size1, sizeof(int), cmpfunc);
        qsort(list2, size2, sizeof(int), cmpfunc);
        
        int diff, i=0, j=0, start =0, differ;
        //find the first element of the first list that is larger than the smallest element of the second list. 
        while(list1[i] < list2[0] && i < size1) {
            i++;
        }
        start = i; 
        if(start == size1) {
            return -1; 
        }
        else {
            diff = list1[start] - list2[0];
            (*pair)[0] = list1[start];
            (*pair)[1] = list2[0];
            for(i = start; i < size1; i++) {
                for(j = 0; j < size2; j++) {
                    if(list1[i] < list2[j]) {
                        break; 
                    }
                    else {
                        differ = list1[i] - list2[j];
                        if(differ < diff) {
                            diff = differ;
                            (*pair)[0] = list1[i];
                            (*pair)[1] = list2[j];
                        }
                    }
                }
            }
            return diff; 
        }
    }
}
int cmpfunc (const void * a, const void * b)
{
   return ( *(int*)a - *(int*)b );
}