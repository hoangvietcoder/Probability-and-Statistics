import itertools
from fractions import Fraction


# Cho một bình kín có 9 quả banh: 2 quả màu trắng, 3 quả xanh dương và 4 quả màu đỏ. Biết
# rằng mỗi quả có xác suất được chọn như nhau.

def cross(A, B):
    return {a + b for a in A for b in B}


# #a/ Tạo một tập hợp để lưu các quả banh. Ký hiệu 2 quả banh màu trắng là 'W1', 'W2'. Tương
# tự cho 3 quả xanh dương là 'B1', 'B2', 'B3' và 4 quả màu đỏ là 'R1', 'R2', 'R3'. 'R4'. Lưu vào
# biến URN.

URN = cross('W', '12') | cross('B', '123') | cross('R', '1234')
print("a.", URN)

# b/ Tìm tập con gồm 3 quả banh từ tập hợp URN trên (không phân biệt thứ tự). Lưu kết quả
# của tập con đó vào biến U3.

U3 = list(itertools.combinations(URN, 3))
print("b.", len(U3))

# c/ Liệt kê các trường hợp 3 quả banh được chọn ở câu (b) có một quả banh màu trắng, một
# quả banh màu xanh dương và một quả banh màu đỏ, kết quả lưu vào biến white1blue1red1.

white1blue1red1 = []
for j in U3:
    if j[0][0] != j[1][0] and j[0][0] != j[2][0] and j[1][0] != j[2][0]:
        white1blue1red1.append(j)
print("c.", white1blue1red1)

# d/ Tính xác suất chọn ngẫu nhiên 3 quả banh trong đó có một quả banh màu trắng, một quả
# banh màu xanh dương và một quả banh màu đỏ, kết quả lưu vào biến P.

count = 0
for k in U3:
    if k[0][0] != k[1][0] and k[0][0] != k[2][0] and k[1][0] != k[2][0]:
        count += 1
P = Fraction(count, len(U3))
print("d.", P)
