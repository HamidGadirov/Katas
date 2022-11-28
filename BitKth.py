# Given array of integers, remove each kth element from it.

def solution(a, k):
    aRemoved = []
    for i in range(len(a)):
        if (i + 1) % k != 0:
            aRemoved.append(a[i])
    return aRemoved
    
    # del inputArray[k-1::k] # k-1 th of every k elements

#  Kill K-th Bit
#  It's now up to you to write a function that will change the kth bit of n back to 0.
def solution(n, k):
    return n & ~(1<<(k-1))