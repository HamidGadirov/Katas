
# Mutable, non-ordered, unique

set.add(elem)

'''
Scholarships are considered to be correctly distributed if all best students have it, 
but not all students in the university do. Obviously, only university students should be able to get a scholarship, 
i.e. there should be no outsiders in the list of the students that will get a scholarships.
'''
def solution(bestStudents, scholarships, allStudents):
    return set(bestStudents).issubset(set(scholarships)) and (set(scholarships).issubset(set(allStudents)) and set(allStudents).difference(set(scholarships)) != set())
    # return set(bestStudents) <= set(scholarships) < set(allStudents)

# difference is same as '-'

'''
You want to use only popular characters in the name of your company, but not too mainstream. 
You consider a character to be popular if it appears in at least two company names, and consider it to be mainstream if it appears in all three.
'''
def solution(companies):
    cmp1 = set(companies[0])
    cmp2 = set(companies[1])
    cmp3 = set(companies[2])
    res = (cmp1 & cmp2 | cmp1 & cmp3 | cmp2 & cmp3) - (cmp1 & cmp2 & cmp3)
    # res = ((cmp1 | cmp2 | cmp3) - (cmp1 ^ cmp2 ^ cmp3))
    return list(sorted(list(res)))