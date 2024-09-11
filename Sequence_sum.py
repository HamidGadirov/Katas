"""
Given a non-empty list of positive integers l and a 
target positive integer t, write a function solution(l,
 t) which verifies if there is at least one consecutive
 sequence of positive integers within the list l (i.e. 
a contiguous sub-list) that can be summed up to the 
given target positive integer t (the key) and returns 
the lexicographically smallest list containing the 
smallest start and end indexes where this sequence can 
be found, or returns the array [-1, -1] in the case 
that there is no such sequence (to throw off Lambda's 
spies, not all number broadcasts will contain a coded 
message).

-- Python cases --
Input:
solution.solution([1, 2, 3, 4], 15)
Output:
-1,-1
Input:
solution.solution([4, 3, 10, 2, 8], 12)
Output:
2,3
"""

import queue


def solution(l, t):
    start = stop = 0
    while start <= stop and stop < len(l):
        s = sum(l[start:stop+1])
        if s == t:
            return [start, stop]
        elif s < t:
            stop += 1
        else:
            start += 1
            stop = max(start, stop)
    
    return [-1, -1]

def solution_queue(l, t):
    queue = []
    sum = 0
    for i, elem in enumerate(l):
        # print(elem)
        queue.append(elem)
        sum += elem
        if sum > t:
            sum -= queue.pop(0)
            # print(sum)
        if sum == t:
            return i + 1 - len(queue), i
    
    return [-1, -1]

print(solution_queue([250,0,0], 250))
print(solution_queue([1,2,3,4], 15))
print(solution_queue([4, 3, 10, 2, 8], 12))
print(solution_queue([4, 3, 5, 7, 8], 12))
print(solution_queue([260], 260))

'''
[0, 0]
[-1, -1]
[2, 3]
[0, 2]
[0, 0]
'''