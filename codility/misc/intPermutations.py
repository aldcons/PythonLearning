#! python

#Can't remember where I found this exercise but think it may have been on Codility.
#Return the largest number for the different permutations of an interger.
#For e.g. int 365 - can be arranged as 356, 563, 536, 653, 635 the biggest would be returned - IE 653 


def solution(N):
    from itertools import permutations
    lenN = len(str(N))
    combos = []
    largest = N
    for p in permutations(str(N)):
        #string_list = [''.join(item) for item in tuple_list]
        combos = [''.join(p) for p in permutations(str(N))]
    for combo in combos:
        if int(combo) > largest:
            largest = int(combo)
    return largest

    
A = 100089
print (solution(A))
