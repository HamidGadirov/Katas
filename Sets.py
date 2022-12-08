
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