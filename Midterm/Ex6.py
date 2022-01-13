import itertools

# Cho tập hợp E = {0,1,2,3,4,5}
E = {0, 1, 2, 3, 4, 5}
U4 = list(itertools.permutations(E, 4))


# a/Liệt kê các số có 3 chữ số, các chữ số được tạo từ các phần tử trong tập hợp E.

def cross(A, B, C):
    return {int(a + b + c) for a in A for b in B for c in C}


def Cau6a():
    print("a.", cross('12345', '012345', '012345'))


# b/Liệt kê các số có 4 chữ số (đôi một khác nhau), các chữ số được tạo từ các phần tử trong tập hợp E
def Cau6b():
    tmp = []
    for i in U4:
        if i[0] != 0:
            tmp.append((i[0] * 1000 + i[1] * 100 + i[2] * 10 + i[3]))
    print("b.", tmp)


Cau6a()

print()

Cau6b()
