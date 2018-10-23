#! python

#total = 100% 
#https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

from sys import maxsize 
def solution(a): 
    size = len(a)   
    max_so_far = -maxsize - 1
    max_ending_here = 0
       
    for i in range(0, size): 
        max_ending_here = max_ending_here + a[i] 
        if (max_so_far < max_ending_here): 
            max_so_far = max_ending_here 
  
        if max_ending_here < 0: 
            max_ending_here = 0   
    return max_so_far   
        
       
A = [3, 2, -6, 4, 0]

print (solution(A))
