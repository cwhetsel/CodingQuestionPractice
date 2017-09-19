# Question: Can you write a function to swap two numbers in place (without temporary variables)
### Time To complete: ~15 minutes 
### 9/19/17

___

Done in JAVA, C, and Python

Essentialy you use algebra. You have 3 varibales and 2 knowns at anyone time. That means you can always find out the last variable
First, do first + second = sum and put it into the first position. 
then to put the first number into the second position, first = sum - second 
finally to get the second number back and in the first position, second = sum - first
 
 ```python
 def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b
```
