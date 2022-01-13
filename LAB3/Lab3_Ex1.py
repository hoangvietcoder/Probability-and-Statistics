from fractions import Fraction


def P(event, space):
    return Fraction(len(event & space), len(space))


S = {'MMM', 'FMM', 'MFM', 'MMF', 'FFF', 'MFF', 'FMF', 'FFM'}
print(len(S))
B = {s for s in S if 'F' in s}
A = {s for s in B if s.count('F') == 3}

P_B = P(B, S)
P_A = P(A, S)
P_female = P_A / P_B

print(P_female)
