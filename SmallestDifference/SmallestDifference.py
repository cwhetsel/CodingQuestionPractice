''' Question: Given two integer arrays, compute the pair of values(one from each array) with the smallest nonnegative difference. Return the difference
    9/25/17
    Time: 30 min 
    Complexity: O(nlogn + llogl)
    A brute force method would be to have a nested loop which calculates the difference of each possible pair and returns the smallest nonnegative. 
    This would run in O(n*l) where is the length of the first list and l is length of the second list. However, we can improve the performance by 
    sorting the arrays first. For this version we will assume that we are taking teh absolute value of the difference not just taking the values of list1-list2
    that are non negative. We will still sort but take the abs value of the differnece, moving the smaller number to the next index to find the 
   smallest difference. Sorting takes 0(nlogn) and finding the smallest takes )(n+l)
'''

def findSmallestDifference(l1: "first list of integers", l2: "second list of integers"):
    l1.sort()
    l2.sort()
    i = 0
    j = 0
    diff = abs(l1[0] - l2[0])
    while(i < len(l1) and j < len(l2)):
        tmp = abs(l1[i] - l2[j])
        if(tmp < diff):
             diff = tmp
        #move the smaller value bc the only way to make the diff smaller is to move the samller value closer to the larger. 
        if(l1[i] < l2[j]):
            i+=1
        else:
            j+=1

    return diff

l1 = [1, 4, 9, 15]
l2 = [9, 2, 17, 22, 90]
print("the smallest difference is " + str(findSmallestDifference(l1, l2)))

