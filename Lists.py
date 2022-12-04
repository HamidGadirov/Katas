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