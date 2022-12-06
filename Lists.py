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