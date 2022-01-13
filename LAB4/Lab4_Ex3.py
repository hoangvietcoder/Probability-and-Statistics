import itertools


def cross(A, B):
    return {a + b for a in A for b in B}


men = cross('M', '1234')
women = cross('W', '12')
member = list(men | women)

permutations_member = list(itertools.permutations(member, 6))
print("a.", len(permutations_member))

solutions_3_men = list()
for s in permutations_member:
    for i in range(len(s)):
        if 'M' in s[i]:
            count = 1
            for j in range(i + 1, len(s)):
                if 'M' not in s[j]:
                    break
                count += 1
            if count == 3:
                solutions_3_men.append(s)
print("b.", len(solutions_3_men))

solutions_2_women = list()
for s in permutations_member:
    for i in range(len(s)):
        if 'W' in s[i]:
            if s[i + 1].count('W') == 0:
                solutions_2_women.append(s)
            break
print("c.", len(solutions_2_women))
