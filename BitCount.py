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
        


