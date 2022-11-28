# Given array of integers, remove each kth element from it.

def solution(a, k):
    aRemoved = []
    for i in range(len(a)):
        if (i + 1) % k != 0:
            aRemoved.append(a[i])
    return aRemoved
    
    # del inputArray[k-1::k]

    