import random
import itertools

Ranks = {'2', '3', '4', '5', '6', '7', '8', '9', 'Jack', 'Queen', 'King', 'Ace'}
Suits = {'Heart', 'Diamond', 'Club', 'Spade'}
Cards = list(itertools.product(Ranks, Suits))
print(len(Cards))


def simualtor_poker(n):
    count = 0
    for i in range(n):
        tmp = []
        for j in range(5):
            index = 0
            random.shuffle(Cards)
            if Cards[index][0] == 'Ace':
                tmp.append(1)
            elif Cards[index][0] == 'Jack':
                tmp.append(2)
            else:
                tmp.append(4)
        if tmp.count(1) == 2 and tmp.count(2) == 3:
            count += 1
    return count / n


print(simualtor_poker(100000))
