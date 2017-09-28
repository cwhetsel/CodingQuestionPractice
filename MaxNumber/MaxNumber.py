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