''' Question: Write methods to implement the multiply subtract and divide operators for integers. The 
    results of all these are integers 
# Time To complete: 15 minutes 
# 9/19/17
'''
#
def multiply(a, b): 
    '''function takes in two integers and their product'''
    if a == 0 or b ==0:
        return 0
    product = 0
    if b > 0:
        for x in range(0,b):
            product += a
    elif a < 0:
        l = len(range(a,0)) + len(range(a,0))
        x=0
        while x < l:
            a += 1
            x+=1
        while b < 0:
            product += a
            b+=1
    else:
        for x in range(0,a):
            product += b
    return product

def subtract(a, b):
    '''Functions calulate subtract b from a where a and b are integers'''
    return a+(multiply(b,-1))

def divide(a: 'Numerator', b: 'Divisor'):
    '''Takes two integers and returns (a-(a%b))/b'''
    if a == 0 or b ==0:
        raise Exception("Divide by zero")
    else:    
        quotient = 0
        negative = False
        if b < 0:
            negative = True
            b = multiply(b,-1)
        while b > 0 and a >= b:
            quotient += 1
            a = subtract(a,b)
        if negative:
            return multiply(quotient, -1)
        return quotient
  

mlist = [1, 2, -2, 3, -3]
print(mlist)

for x in mlist:
    for y in mlist:
        print("a= " + str(x) + " b= " + str(y))
        print("Subtract: " + str(subtract(x,y)))
        print("Multiply: " + str(multiply(x,y)))
        print("Divide: " + str(divide(x,y)))

