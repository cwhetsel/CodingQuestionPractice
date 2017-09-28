/*
    Question: Write an algorithm which computes the number of trailing zeros in a factorial 
    Time: 20 min
    9/25/17
    Complexity: O(log5(n))

    We will asume we will be given the factorial as 5! and not as the full multiplied form of 5! i.e. 120
    Because it is multiplication, you never lose a 0 once you have it. Also, the factorials get too large so you cannot just
    multiply it all out then count the zeroes at the end. Multiplying two odd number never give you an even. Two evens will give you
    an even but not a trailing zero. You need a five to get a trailing zero. So ever multiple of five, another trailing zero is added
    to the result of expanding the factorial. 0 to 4 factorial have none, 5-9 have 1, 10-14 have 3, 15-19 have 3 and so on. However, 
    powers of 5 contribute more than one five, so you have to count each value of 5, and 25, and 5^x until 5^x is larger than the factorial. 
*/

#import<stdio.h>
#import<stdlib.h>

int countTrailingZeros(int factorial);

int main(int argc, char** argv) {
    int factorial = 75;
    printf("%d has %d trailing zeros", factorial, countTrailingZeros(factorial) );
    

    return (EXIT_SUCCESS);
}

int countTrailingZeros(int factorial) {
    if(factorial < 0) {
        return -1;
    }
    else {
        //you can count the multiples of 5 in a number just by dividing by 5, but you have to remember that 25 contributes 
        // two 5's and 125 contributes 3 and so on. Thus, you have to check each power of 5 that is smaller that the factorial 
        int zeros = 0, div;
        for(div = 5; factorial/div > 0; div *= 5) {
            zeros += (int)(factorial/div);
        }
        return zeros;
    }
}