import random


def simualtor_dice5(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 + dice2 > 6:
            count += 1
    return count / n


print(simualtor_dice5(1))
print(simualtor_dice5(10))
print(simualtor_dice5(100))
print(simualtor_dice5(1000))
print(simualtor_dice5(10000))
print(simualtor_dice5(100000))
