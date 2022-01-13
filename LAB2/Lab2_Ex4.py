import random


def simualtor_dice4(n):
    count = 0
    for i in range(n):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        if dice1 == 1 and dice2 == 6 or dice1 == 6 and dice2 == 1:
            count += 1
    return count / n


print(simualtor_dice4(1))
print(simualtor_dice4(10))
print(simualtor_dice4(100))
print(simualtor_dice4(1000))
print(simualtor_dice4(10000))
print(simualtor_dice4(100000))
