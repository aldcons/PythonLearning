#! Python 

#Second attempt  -see first attempt below - using collections
###Taken from codesays.com - Better best 
#Lost link - update with link when found.
def solution(A):
    A_len = len(A)
    candidate = -1
    candidate_count = 0
    candidate_index = -1
    # Find out a leader candidate
    for index in range(A_len):
        if candidate_count == 0:
            candidate = A[index]
            candidate_index = index
            candidate_count += 1
        else:
            if A[index] == candidate:
                candidate_count += 1
            else:
                candidate_count -= 1
    # Make sure the candidate is the leader
    leader_count = len([number for number in A if number == candidate])
    if leader_count <= A_len//2:
        # The candidate is not the leader
        return 0
    else:
        leader = candidate
    equi_leaders = 0
    leader_count_so_far = 0
    for index in range(A_len):
        if A[index] == leader:
            leader_count_so_far += 1
        if leader_count_so_far > (index+1)//2 and leader_count-leader_count_so_far > (A_len-index-1)//2:
            # Both the head and tail have leaders of the same value
            # as "leader"
            equi_leaders += 1
    return equi_leaders   

A = [4, 4, 2, 5, 3, 4, 4, 4]

print (solution(A))




##first attempt 100% 0% on performance
#def solution(A):
#    from collections import Counter
#    N = len(A)
#    inBoth = 0
#    for i in range(1, N):
#        seqA = (A[:i])
#        seqB = (A[i:])
#        
#        #elemA, elemCountA = Counter(seqA).most_common(1)
#        #print (elemA, elemCountA)
#        if  [item[0] for item in (Counter(seqA).most_common(1))] == [item[0] for item in (Counter(seqB).most_common(1))]:
#            countItemA = [item[1] for item in (Counter(seqA).most_common(1))][0]
#            countItemB = [item[1] for item in (Counter(seqB).most_common(1))][0]
#            if countItemA / len(seqA) > 0.5:
#                if countItemB / len(seqB) > 0.5:
#                #print (seqA, countItemA, seqB, countItemB)
#                    inBoth = inBoth + 1
#        
#        #print  (seqA, [item[1] for item in (Counter(seqA).most_common(1))], seqB, [item[1] for item in (Counter(seqB).most_common(1))])
#           # print 
#    return inBoth    
#       
#A = [4, 4, 2, 5, 3, 4, 4, 4]
#
#print (solution(A))


