import itertools


def cross(A, B):
    return {a + b for a in A for b in B}


urn = cross('1', 'ABCD') | cross('2', 'ABCD') | cross('3', 'ABCD') | cross('4', 'ABCD') | cross('5', 'ABCD')
combinations_q_a = list(itertools.combinations(urn, 5))

count_1 = 0
for s1 in combinations_q_a:
    tmp_1 = list()
    for i1 in range(5):
        tmp_1 += s1[i1][0]
        if tmp_1.count('1') == 1 and tmp_1.count('2') == 1 and tmp_1.count('3') == 1 and tmp_1.count('4') == 1 and tmp_1.count('5') == 1 and len(tmp_1) == 5:
            count_1 += 1
print("a.", count_1)


urn_wrong = cross('1', 'BCD') | cross('2', 'ACD') | cross('3', 'ABC') | cross('4', 'ABD') | cross('5', 'ABD')
combinations_q_a_wrong = list(itertools.combinations(urn_wrong, 5))

count_2 = 0
for s2 in combinations_q_a_wrong:
    tmp_2 = {s2[0][0], s2[1][0], s2[2][0], s2[3][0], s2[4][0]}
    if len(tmp_2) == 5:
        count_2 += 1
print("b.", count_2)
