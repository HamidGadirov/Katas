# Given an array a that contains only numbers in the range from 1 to a.length, find the first duplicate number for which the second occurrence has the minimal index. In other words, if there are more than 1 duplicated numbers, return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. If there are no such elements, return -1.

# Example
# For a = [2, 1, 3, 5, 3, 2], the output should be solution(a) = 3.

def solution(a):
    # a_set = set(a)
    # a_set_list = list(a_set)
    # duplicates = []
    # for i in range(len(a_set_list)):
    #     count = 0
    #     index = 0
    #     for j in range(len(a)):
    #         if a_set_list[i] == a[j]:
    #             # print(j, a[j])
    #             count += 1
    #             if count == 1:
    #                 index = j
    #             if count == 2:
    #                 duplicates.append(a[j])
    # # print(duplicates)
    # if len(duplicates) == 0:
    #     return -1
    
    # min_distance = len(a)
    # number = 0
    # for d in range(len(duplicates)):
    #     distance = 0
    #     foundDuplicate = False
    #     for i in range(len(a)):
    #         if duplicates[d] == a[i] and foundDuplicate == False:
    #             foundDuplicate = True
    #             # print(i)
    #             continue
    #         if foundDuplicate:
    #             distance += 1
    #             # print(distance)
    #         if duplicates[d] == a[i] and foundDuplicate == True:
    #             if min_distance > distance:
    #                 min_distance = distance
    #                 number = a[i]
    # return number
        
    # before = []            
    # for i in range(len(a)):
    #     before.append(a[i])
    #     for j in range(len(before) - 1):
    #         if a[i] == before[j]:
    #             # print(j, before[j])
    #             return a[i]
    # return -1
    
    a_set = set()
    for el in a:
        if el in a_set:
            return el
        a_set.add(el)
    return -1
            
        

