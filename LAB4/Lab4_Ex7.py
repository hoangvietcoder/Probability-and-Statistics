import itertools
from fractions import Fraction


def P(event, space):
    return Fraction(len(event & space), len(space))


Suits = ['Heart', 'Diamond', 'Clud', 'Spades']
Ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
Cards = list(itertools.product(Ranks, Suits))

permutations_cards = list(itertools.permutations(Cards, 3))

A1 = list()
for i in permutations_cards:
    if i[0][0] == 'Ace' and (i[0][1] == 'Heart' or i[0][1] == 'Diamond'):
        A1.append(i)

P_A1 = Fraction(len(A1), len(permutations_cards))
print("a.", round(float(P_A1), 4))

A2 = list()
for i in permutations_cards:
    if i[1][0] == '10' or i[1][0] == 'Jack':
        A2.append(i)

P_A2 = Fraction(len(A2), len(permutations_cards))
print("b.", round(float(P_A2), 4))

A3 = list()
for i in permutations_cards:
    if '3' < i[2][0] < '7':
        A3.append(i)

P_A3 = Fraction(len(A3), len(permutations_cards))
print("c.", round(float(P_A3), 4))

A = list()
for i in permutations_cards:
    if (i[0][0] == 'Ace' and (i[0][1] == 'Heart' or i[0][1] == 'Diamond')) and (i[1][0] == '10' or i[1][0] == 'Jack') and (
            '3' < i[2][0] < '7'):
        A.append(i)
P_A = Fraction(len(A), len(permutations_cards))
print("d.", round(float(P_A), 4))
