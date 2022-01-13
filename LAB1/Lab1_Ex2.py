import itertools


def cross(A, B):
    return {a + b for a in A for b in B}


urn = cross('W', '12345678') | cross('B', '123456') | cross('R', '123456789')
# a
U3 = list(itertools.combinations(urn, 3))
for i in U3:
    print(i)
len_U3 = len(U3)
print(len_U3)

# b
count = 0
for j in U3:
    if j[0][0] != j[1][0] and j[0][0] != j[2][0] and j[1][0] != j[2][0]:
        count = count + 1
        print(j)
print(count)

# c
c = 0
for u in U3:
    if u[0][0] == 'W' and u[1][0] == 'R':
        print(u)
        c = c + 1
print(c)
