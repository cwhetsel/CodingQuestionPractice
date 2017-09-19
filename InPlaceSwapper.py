# Question: Can you write a function to swap two numbers in place (without temporary variables)
# Time To complete: 15 minutes 
# 9/19/17

#function takes in two integers and returns a tuple of them swapped without temp vars
def swap(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

mlist = [1, 2, 2.5, 3, 3.5]
print(mlist)

print("Swap 0, 1")
mlist[0], mlist[1] = swap(mlist[0], mlist[1])
print(mlist)
print("Swap 0, 4")
mlist[0], mlist[4] = swap(mlist[0], mlist[4])
print(mlist)