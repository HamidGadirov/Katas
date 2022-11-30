# Given an array of equal-length strings, you'd like to know if it's possible to rearrange the order of the elements in such a way 
# that each consecutive pair of strings differ by exactly one character. Return true if it's possible, and false if not.

# Example
# For inputArray = ["aba", "bbb", "bab"], the output should be
# solution(inputArray) = false.

import itertools
# def solution(a):
#     for x in itertools.permutations(a):
#         print(x)
#         flag = True
#         for i in range(len(x) - 1):
#             count = 0
#             for j in range(len(x[i])):
#                 if x[i][j] != x[i + 1][j]:
#                     count += 1
#                     if count > 1:
#                         flag = False
#                         break
#             if count != 1:
#                 flag = False
#                 break
#         if flag:
#             return True
#     if not flag:
#         return False
        
def diff(w1, w2):
    return sum([a[0] != a[1] for a in zip(w1, w2)]) == 1

def solution(a):
    for z in itertools.permutations(a):
        if sum([diff(*x) for x in zip(z, z[1:])]) == len(a) - 1:
            return True
    return False


# Define a word as a sequence of consecutive English letters. Find the longest word from the given string.
    return max(re.split('[^a-zA-Z]', text), key=len)

# Help Ratiorg by writing a function that returns the sum of numbers that appear in the given inputString.

def solution(s):
    Sum = 0
    integer = "0"
    for c in s:
        if c.isdigit():
            integer += c
        else:
            Sum += int(integer)
            integer = "0"
    Sum += int(integer)
    return Sum
    
    l = re.findall(r"\d+",inputString)
    return sum([int(i) for i in l])
    
    return sum(map(int,"".join([i if i.isdigit() else " " for i in s]).split()))
    # map() function returns a map object(which is an iterator) of the results 
    # after applying the given function to each item of a given iterable (list, tuple etc.)
                    

