import itertools


# Create input
def cross(A, B):
    return {a + b for a in A for b in B}


math = cross('M', '1234')
physics = cross('P', '123')
chemistry = cross('C', '12')
language = cross('D', '1')

per_math = list(itertools.permutations(math, 4))
per_physics = list(itertools.permutations(physics, 3))
per_chemistry = list(itertools.permutations(chemistry, 2))
per_language = list(itertools.permutations(language, 1))

per_group = list(itertools.permutations({4, 3, 2, 1}, 4))

per_output = []
for i in per_group:
    tmp = []
    for j in i:
        if j == 4:
            tmp.append(per_math)
        elif j == 3:
            tmp.append(per_physics)
        elif j == 2:
            tmp.append(per_chemistry)
        else:
            tmp.append(per_language)
    for j in cross(tmp[0], cross(tmp[1], cross(tmp[2], tmp[3]))):
        per_output.append(j)
print(*per_output, sep='\n')
print(len(per_output))
