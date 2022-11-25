# Given a string s consisting of small English letters, find and return the first instance of a non-repeating character in it. If there is no such character, return '_'.

# Example
# For s = "abacabad", the output should be
# solution(s) = 'c'.

def solution(s):
    # for i in range(len(s)):
    #     nonRepeated = False
    #     for j in range(i, len(s)):
    #         c = s[i]
    #         if c == s[j]:
    #             nonRepeated = True
    #     if not nonRepeated:
    #         return c
    # return '_'
    
# index searches the array for the object starting at element 0 and working up, where rindex will start at the end of the array and work down searching for the object. 
    
    for c in s:
        if s.index(c) == s.rindex(c):
            return c
    return '_'

