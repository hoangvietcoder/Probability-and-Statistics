import random
import itertools

# Giả sử làm thí nghiệm rút 4 là bài từ bộ bài 52 lá, hãy viết hàm tính xác suất thực nghiệm với 
# n lần thí của các sự kiện sau:

Ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
Suits = {'Heart', 'Diamond', 'Club', 'Spade'}
Cards = list(itertools.product(Ranks, Suits))


def checkColor(X):
    result = []
    for x in X:
        if x == 'Club' or x == 'Spade':
            result.append('Black')
        else:
            result.append('Red')
    return result


# a/Bốn lá cùng chất

def Cau3a(n):
    count = 0
    for i in range(n):
        U4 = random.sample(Cards, 4)
        standardize_joined = ''.join([x[1] for x in U4])
        if (standardize_joined.count('Heart') == 4 or standardize_joined.count(
                'Diamond') == 4 or standardize_joined.count('Club') == 4 or standardize_joined.count('Spade') == 4):
            count += 1
    print("a. ", count / n)


Cau3a(1000000)


# b/Bốn lá đôi một khác chất

def Cau3b(n):
    count = 0
    for i in range(n):
        U4 = random.sample(Cards, 4)
        standardize = [x[1] for x in U4]
        if len(set(standardize)) == 4:
            count += 1
    print("b. ", count / n)


Cau3b(1000000)


# c/Bốn lá cùng màu

def Cau3c(n):
    count = 0
    for i in range(n):
        U4 = random.sample(Cards, 4)
        standardize = [x[1] for x in U4]
        if ''.join(checkColor(standardize)).count('Black') == 4 or ''.join(checkColor(standardize)).count('Red') == 4:
            count += 1
    print("c. ", count / n)


Cau3c(1000000)


# d/Bốn lá cùng chỉ số (tứ quý)

def Cau3d(n):
    count = 0
    for i in range(n):
        U4 = random.sample(Cards, 4)
        rank_standardize = [x[0] for x in U4]
        if len(set(rank_standardize)) == 1:
            count += 1
    print("d. ", count / n)


Cau3d(1000000)


# e/Bốn lá cùng là loại số

def Cau3e(n):
    count = 0
    for i in range(n):
        U4 = random.sample(Cards, 4)
        rank_standardize = [x[0] for x in U4]
        if max(rank_standardize) < 11:
            count += 1
    print("e. ", count / n)


Cau3e(1000000)


# f/Bốn lá cùng là loại hình
def Cau3f(n):
    count = 0
    for i in range(n):
        U4 = random.sample(Cards, 4)
        rank_standardize = [x[0] for x in U4]
        if min(rank_standardize) >= 11:
            count += 1
    print("f. ", count / n)


Cau3f(1000000)
