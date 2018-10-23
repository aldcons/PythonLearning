#! Python

#Third 100% with this one!!!
#Can't find original link for this one!!
#Will update with link to original work when found!

def solution(A):
    stack = []
    for a in A:
        stack.append(a)
        while len(stack) > 1 and stack[-1] != stack[-2]:
            stack.pop(),stack.pop()
    if stack:
        candidate, total = stack[0], 0
        for index, a in enumerate(A):
            total += 1 if  a == candidate else 0
            if total > len(A)/2:
                return index
    return -1
        
A = [3, 3, 4, 2, 3, 3, 2, 3]


print (solution(A))

#Second  attempt Correctness 75% and 100% on performance 83% total
#https://github.com/Dineshkarthik/codility_training/blob/master/Lesson%2008%20-%20Leader/dominator.py

#def solution(A):
#    if len(A) == 0:
#        return -1
     
#    sorted_a = sorted(A)
#    l = (len(sorted_a) // 2)
#    test_candidate = sorted_a[l]
   # print (test_candidate, A.count(test_candidate))
#    if A.count(test_candidate) > 1:
#        return A.index(test_candidate)
#    return -1


#A = [3, 3, 4, 2, 3, 3, 2, 3]


#print (solution(A))


#First attempt 100% correct 0% performance 66% total
#def solution(A):
#    N = len(A)
#    indexNum = []
#    count = 0 
#    for num in A:
        #print (num, A.count(num), A.index(num))
#        if A.count(num) > N/2:
#            indexNum.append(count)
#        count = count + 1    
#    if len(indexNum) != 0:
#        return indexNum[0]
#    else:
#        return -1



#A = [2, 3, 3, 2, 3, 3, 2, 3]


#print (solution(A))





