import itertools
import random

# Cho bộ bài tây 52 lá. Rút ngẫu nhiên 5 lá bài. Tính xác suất 5 lá bài tạo thành một sảnh.

Ranks = {2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14}
Suits = {'Heart', 'Diamond', 'Club', 'Spades'}
Cards = list(itertools.product(Ranks, Suits))


# a/ Xác suất lý thuyết.

def Cau5a():
    count = 0
    U5 = list(itertools.combinations(Cards, 5))
    for i in range(len(U5)):
        standardize = [x[0] for x in U5[i]]
        if (max(standardize) - min(standardize) == 4) and min(standardize) != 2 and len(set(standardize)) == 5:
            count += 1
    print("P = ", count / len(U5))


# b/Xác suất thực nghiệm
def Cau5b(n):
    count = 0
    for i in range(n):
        pick5 = random.sample(Cards, 5)
        standardize = [x[0] for x in pick5]
        if (max(standardize) - min(standardize) == 4) and min(standardize) != 2 and len(set(standardize)) == 5:
            count += 1
    print("P = ", count / n)


Cau5a()
Cau5b(1000000)
