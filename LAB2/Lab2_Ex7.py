import itertools
import random

Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'heart', 'diamond', 'clubs', 'spades'}
Cards = list(itertools.product(Ranks, Suits))


def simulator_poker2(n):
    count = 0
    for i in range(n):
        tmp = []
        for j in range(4):
            index = 0
            random.shuffle(Cards)
            if Cards[index][1] == 'heart':
                tmp.append(1)
            elif Cards[index][1] == 'diamond':
                tmp.append(2)
            elif Cards[index][1] == 'clubs':
                tmp.append(3)
            else:
                tmp.append(4)

        a = set(tmp)
        if len(a) == 4:
            count += 1
    return count / n


print(simulator_poker2(100))
print(simulator_poker2(1000))
print(simulator_poker2(10000))
print(simulator_poker2(100000))
print(simulator_poker2(1000000))
