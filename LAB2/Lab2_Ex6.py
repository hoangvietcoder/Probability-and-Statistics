import itertools
import random

Ranks = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K'}
Suits = {'heart', 'diamond', 'clubs', 'spades'}
Cards = list(itertools.product(Ranks, Suits))


def simulator_poker1(n):
    count = 0
    for i in range(n):
        tmp = []
        for j in range(5):
            index = 0
            random.shuffle(Cards)
            if Cards[index][1] == 'heart':
                tmp.append(Cards[index])
            if len(set(tmp)) == 5:
                count += 1
    return count / n


print(simulator_poker1(10))
print(simulator_poker1(100))
print(simulator_poker1(1000))
print(simulator_poker1(10000))
print(simulator_poker1(1000000))
