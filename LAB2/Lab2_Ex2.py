import random


def simualtor_dice2(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 % 2 == 0 and dice2 % 2 == 1 or dice1 % 2 == 1 and dice2 % 2 == 0:
            count += 1
    return count / n


print(simualtor_dice2(1))
print(simualtor_dice2(10))
print(simualtor_dice2(100))
print(simualtor_dice2(1000))
print(simualtor_dice2(10000))
print(simualtor_dice2(100000))
