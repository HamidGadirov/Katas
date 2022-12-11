# Lists Concatenation
list1.extend(list2)

# comprehension
new_l = [x + 1 if x >= 45 else x + 5 for x in l]

# create with specific size
w, h = 8, 5
Matrix = [[0 for x in range(w)] for y in range(h)] 

sum([students[i] for i in range(len(students)) if i % 2 == 0]) - sum([students[i] for i in range(len(students)) if i % 2 == 1])
# is same as
sum(students[::2])-sum(students[1::2])

# Given the list of task ids in your toDo list, remove each kth task from it and return the list of remaining tasks.
del toDo[k-1::k]

def solution(n):
    return [[i * j for j in range(1, n + 1)] for i in range(1, n + 1)]

# comprehension can be used with dict and set:
def solution(word):
    num = {chr(ord('a') + i): i + 1 for i in range(26)}
    return sum([num[ch] for ch in word])

def solution(a, b):
    uniqueSums = {i + j for i in a for j in b if (i * j) % (i + j) == 0}

def solution(n):
    return [[0] * min(i + 1, 2 * n - (i + 1)) for i in range(n * 2 - 1)]

def solution(ch, assignments):
    return [ch * assignments[i] for i in range(len(assignments))]
    # return [ch * d for d in data]
    # return list(map(lambda i: i * ch, data))

# Least Common Denominator
from math import gcd

def solution(denominators):
    return functools.reduce(lambda a, b: a * b // gcd(a, b) if a % b != 0 else a, denominators)

print("The maximum element of the list is : ", end="")
print(functools.reduce(lambda a, b: a if a > b else b, lis))

# Transpose Dictionary
def solution(scriptByExtension):
    return sorted([(v, k) for k, v in scriptByExtension.items()])
    # return sorted(zip(scriptByExtension.values(), scriptByExtension.keys()))
    # return sorted([[value, key] for key, value in scriptByExtension.items()])


# Given a list of digits as they are written in the clockwise order, find all other combinations the password could possibly have.
from collections import deque
def solution(digits):
    n = len(digits)
    res = [deque(digits) for _ in range(n)]
    deque(map(lambda i: res[i].rotate(-i), range(n)), 0)
    return [list(d) for d in res]