/* Question: Write a method that finds the max of two numbers. You shouls not use if-else or any other comparison operator    
    9/28/17
    Time: 40 min 
    Complexity: O(nlogn + llogl)

    Maybe you could use the difference of the numbers in some way? check the bits? We could use the sign bit of the 
    difference to tell if it is positive or negative which will tell us which is the larger. The sign bit could 
    also act as our true false value. like return k*a + b*(1-k) so when k is 1 it returns a bc its larger, 
    but when k = 0 it returns b. Basically like an if else but with math. But how to get the sign bit. 
    We could convert the result to binary somehow. If we could get the negative flag from the adder we could use 
    that but I have no idea how to get to that. 

    Answer. I had to look this one up because I was unfamiliar with bit manipulation in C. This question doesnt make much 
    sense for python because integers in python 3 do not really have a max size so there is no good way of getting 
    the sign bit without comparison operators.  
    & - and, | - or, ~ - flip, ^ - xor, << >> - shift  
*/


int flip(int bit) {
    //if bit is 1 then return 0 bc its in both, if it is 0 returns 1 bc 0 XoR 1 = 1
    return 1^bit;
}
//shifts a 31 bits to the left so its first bit is now in position 2^0 and it is compared with 0x1 aka 1
//do 31 because int's are 32 bits in c 
//it flips the result because the if the number starts with 0 then it is positive. If it starts with 1 it is negative 
//and we want to use this on the result of a-b, so this to return 1 when a is larger than b whihc would 
//mean it is a positive number and would return 0 if we did not flip. 
int sign(int a) {
    return flip((a>>31) & 0x1)
}

//we have to be careful of overflow if the signs of a and b are different. If a and b have different signs we will 
// use the sign of a because the result should stay the same sign as a.
// else we will use the sign of a-b because overflow is implossible. 
int getMax(int a, int b) {
    int c = a-b;
    int sa = sign(a);
    int sb = sign(b);
    int sc = sign(c);

    //if a and b have different signs, we use this. Use XOR
    int use_signa = sa^sb;
    
    // if a and b have same sign we use this. !XOR
    int use_signc = flip(sa^sb);

    //multiplication to zero out the value we dont want to use. 
    int k = use_signa*sa + use_signc*sc

    //k= 0 return b k=1 return a
    return a*k + b(1-k);
}
