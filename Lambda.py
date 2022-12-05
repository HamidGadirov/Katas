# Your task is to sort the students lexicographically by their surnames. 
# If two students happen to have the same surname, their order in the result should be the same as in the original list.

def solution(students):
    students.sort(key=lambda students: students.split(' ')[-1])
    # students.sort(key=lambda s: s.split()[-1])
    return students


# sorting using custom key
employees = [
    {'Name': 'Alan Turing', 'age': 25, 'salary': 10000},
    {'Name': 'Sharon Lin', 'age': 30, 'salary': 8000},
    {'Name': 'John Hopkins', 'age': 18, 'salary': 1000},
    {'Name': 'Mikhail Tal', 'age': 40, 'salary': 15000},
]

# sort by name (Ascending order)
employees.sort(key=lambda x: x.get('Name'))
print(employees, end='\n\n')

# sort by Age (Ascending order)
employees.sort(key=lambda x: x.get('age'))
print(employees, end='\n\n')

# sort by salary (Descending order)
employees.sort(key=lambda x: x.get('salary'), reverse=True)
print(employees, end='\n\n')


digitSum = lambda x: sum([int(c) for c in str(x)])
# is same as
digitSum = lambda r: sum(map(int,str(r)))