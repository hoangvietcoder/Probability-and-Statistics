import itertools
import random


# # Cho một bình kín có 2 bi xanh, 3 bi đỏ và 5 bi trắng. Giả sử bốc 3 viên bi từ trong bình. Hãy
# # viết hàm tính xác suất thực nghiệm với n lần thí nghiệm của các sự kiện sau:

def cross(A, B):
    return {a + b for a in A for b in B}


urn = cross('W', '12345') | cross('B', '12') | cross('R', '123')
U3 = random.sample(urn, 3)


# a/Cả ba viên cùng màu

def Cau2a(n):
    count = 0
    for i in range(n):
        U3 = random.sample(urn, 3)
        if (U3[0][0] == U3[1][0] and U3[1][0] == U3[2][0] and U3[0][0] == U3[2][0]):
            count += 1
    print("a.", count / n)


Cau2a(1000000)


# b/Cả ba viên đều khác màu nhau

def Cau2b(n):
    count = 0
    for i in range(n):
        U3 = random.sample(urn, 3)
        if U3[0][0] != U3[1][0] and U3[1][0] != U3[2][0] and U3[0][0] != U3[2][0]:
            count += 1
    print("b.", count / n)


Cau2b(1000000)


# c/ Chỉ có hai viên cùng màu

def Cau2c(n):
    count = 0
    for i in range(n):
        U3 = random.sample(urn, 3)
        U3_joined = ''.join(random.sample(urn, 3))
        if U3_joined.count('R') == 2 or U3_joined.count('W') == 2 or U3_joined.count('B') == 2:
            count += 1
    print("c.", count / n)


Cau2c(1000000)


# d/Được 2 bi đỏ và 1 bi trắng

def Cau2d(n):
    count = 0
    for i in range(n):
        U3 = random.sample(urn, 3)
        U3_joined = ''.join(random.sample(urn, 3))
        if U3_joined.count('R') == 2 and U3_joined.count('W') == 1:
            count += 1
    print("d.", count / n)


Cau2d(1000000)


# e/Liệt kê các trường hợp 3 bi đều màu trắng.

def Cau2e(n):
    count = 0
    for i in range(n):
        U3 = random.sample(urn, 3)
        U3_joined = ''.join(random.sample(urn, 3))
        if U3_joined.count('W') == 3:
            count += 1
    print("e.", count / n)


Cau2e(1000000)
