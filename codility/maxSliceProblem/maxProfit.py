#! python

#Second attempt Correct 80% Performance 100% - total 88%
#Third attempt same but with len == 0 check
#Max profit = maxP
#Min Price = minP
#https://www.geeksforgeeks.org/maximum-difference-between-two-elements/

def solution(A):
    maxProf = 0
    
    if len(A) == 0:
        #added on third attempt
        return maxProf  
    minProf = A[0]
    
    for i in range(1, len(A)):    
        if A[i] - minProf > maxProf:
            maxProf = A[i] - minProf
        if A[i] < minProf:
            minProf = A[i]
    return maxProf                

#A = []
A = [23171, 21011, 21123, 21366, 21013, 21367]
#A = [5, 4, 3, 2, 1]

print (solution(A))




# First attempt 66% - 100% correct 25% performance
#def solution(A):
#    maxP = 0    
#    for i in range(0, len(A)):
#        for j in range(i + 1, len(A)):
#            if A[j] - A[i] > maxP:
#                maxP = A[j] - A[i]
#    return maxP            
        
  
#A = [23171, 21011, 21123, 21366, 21013, 21367]
#A = [5, 4, 3, 2, 1]

#print (solution(A))
