# Lists Concatenation
list1.extend(list2)

# comprehension
new_l = [x + 1 if x >= 45 else x + 5 for x in l]

# create with specific size
w, h = 8, 5
Matrix = [[0 for x in range(w)] for y in range(h)] 