#! python

#Adapted from https://rafal.io/posts/codility-max-double-slice-sum.html
#Verified on https://codesays.com/2014/solution-to-max-double-slice-sum-by-codility/

def solution(A):
    lenA = len(A)
    newA1 = [0] * (lenA)
    newA2 = [0] * (lenA)
    for i in range(1, lenA - 1 ):
        newA1[i] = max(newA1[i-1] + A[i], 0)
    for i in range(lenA -2, 0, -1):
        newA2[i] = max(newA2[i+1] + A[i], 0)
    maxSum = 0
    for i in range(1, lenA -1):
        maxSum = max(maxSum, newA1[i-1] + newA2[i+1])
    return maxSum
    
A = [3, 2 ,6, -1, 4, 5, -1, 2]
print (solution(A))
