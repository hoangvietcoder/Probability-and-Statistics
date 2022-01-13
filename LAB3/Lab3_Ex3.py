import itertools
from fractions import Fraction


def P(event, space):
    return Fraction(len(event & space), len(space))


suits = ['Heart', 'Diamond', 'Club', 'Spades']
ranks = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
Cards = list(itertools.product(ranks, suits))

B = list(itertools.combinations(Cards, 3))
A1 = set()
for s in B:
    count = 0
    for i in range(3):
        if'King' in s[i]:
            count += 1
    if count == 1 or count == 2:
        A1.add(s)

P_A1 = Fraction(len(A1), len(B))
print(round(float(P_A1), 4))


A2 = set()
for s in B:
    count = 0
    for i in range(3):
        if'King' in s[i]:
            A2.add(s)

P_A2 = Fraction(len(A2), len(B))
print(round(float(P_A2), 4))
