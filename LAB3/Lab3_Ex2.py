from fractions import Fraction


def P(event, space):
    return Fraction(len(event & space), len(space))


S = [('Thanh', 'Nữ'), ('Hồng', 'Nữ'), ('Thương', 'Nữ'), ('Đào', 'Nữ'), ('My', 'Nữ'), ('Yến', 'Nữ'), ('Hạnh', 'Nữ'), ('My', 'Nữ'), ('Vy', 'Nữ'), ('Tiên', 'Nữ'), ('Thanh', 'Nam'), ('Thanh', 'Nam'), ('Bình', 'Nam'), ('Nhật', 'Nam'), ('Hào', 'Nam'), ('Đạt', 'Nam'), ('Minh', 'Nam')]
print(len(S))
A = [s for s in S if 'Thanh' in s]
B = [s for s in S if 'Nữ' in s]
A_B = [s for s in A if 'Nữ' in s]
P_A = Fraction(len(A), len(S))
P_B = Fraction(len(B), len(S))
P_A_B = Fraction(len(A_B), len(S))
print(P_A)
print(P_B)
print(P_A_B)

P_A_with_B = P_A_B / P_B
print(P_A_with_B)
