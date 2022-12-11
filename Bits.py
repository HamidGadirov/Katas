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

# Second-Rightmost Zero Bit Power
def solution(n):
    return (((((n + 1) | n) + 1) | n) - n)

# Swap Adjacent Bits
def solution(n):
    return ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
    # return ((n & 0b10101010101010101010101010101010) >> 1) | ((n & 0b01010101010101010101010101010101) << 1)

# Different Rightmost Bit
def solution(n, m):
    return (n ^ m) & -(n ^ m)
    # XOR and then x & -x gives the rightmost 1

# Rightmost equal pair of bits
def solution(n, m):
    return ~(n ^ m) & ((n ^ m) + 1)
    # XOR: the rightmost 0 bit is the rightmost position of equal bits.
    # complement: the rightmost 1 bit is the rightmost position of equal bits.
    # ~x & (x+1): AND operation with its complement and x+1

# You are given two numbers a and b where 0 ≤ a ≤ b. Imagine you construct an array of all the integers from a to b inclusive. 
# You need to count the number of 1s in the binary representations of all the numbers in the array.
def solution(a, b):
    def bitcount(n):
        count = 0
        while n > 0:
            count = count + 1
            n = n & (n-1)
        return count
        
    def countSetBits(n):
        count = 0
        while (n):
            count += n & 1
            # print("count", count)
            # print("n before", n)
            n >>= 1
            # print("n", n)
        return count
    
    total_ones = 0
    for i in range(a, b + 1):
        # binary = bin(i)[2:]
        total_ones += countSetBits(i)
    return total_ones
    
    # return sum(bin(x).count('1') for x in range(a, b+1))