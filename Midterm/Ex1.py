import random


# Giả sử làm thí nghiệm gieo 2 viên súc sắc, hãy viết hàm tính xác suất thực nghiệm với n lần
# thí nghiệm của các sự kiện sau:

# a/ Hai viên giống nhau
def CauA(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 == die2:
            count += 1
    return count / n


print("a.", CauA(1000000))


# b/ Hai viên khác nhau
def CauB(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 != die2:
            count += 1
    return count / n


print("b.", CauB(1000000))


# c/ Hai viên cùng chẳn
def CauC(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 % 2 == 0 and die2 % 2 == 0:
            count += 1
    return count / n


print("c.", CauC(1000000))


# d/ Hai viên cùng lẻ
def CauD(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 % 2 != 0 and die2 % 2 != 0:
            count += 1
    return count / n


print("d.", CauD(1000000))


# e/ Một viên chẵn và một viên lẻ
def CauE(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 % 2 != 0 and die2 % 2 == 0 or die1 % 2 == 0 and die2 % 2 != 0:
            count += 1
    return count / n


print("e.", CauE(1000000))


# f/ Hai viên cùng ra 6
def CauF(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 == 6 and die2 == 6:
            count += 1
    return count / n


print("f.", CauF(1000000))


# g/ Hai viên có tổng số nút lớn hơn 10
def CauG(n):
    count = 0
    for i in range(n):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        if die1 + die2 > 10:
            count += 1
    return count / n


print("g.", CauG(1000000))
