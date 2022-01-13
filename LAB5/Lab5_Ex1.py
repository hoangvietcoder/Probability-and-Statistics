import math
import numpy as np

print("1a.")
x = np.random.choice([0, 1, 2, 3, 4, 5], 3650, p=[0.1, 0.2, 0.3, 0.2, 0.15, 0.05])
X = set(x)
print(X)

print()

print("1b.")

P = [np.count_nonzero(x == i) / len(x) for i in X]
print(P)

print()

print("1c. ")

E_X = 0
for x in X:
    E_X += x * P[x - 1]
print("Expectation:", E_X)

Var_X = 0
for x in X:
    Var_X += (x - E_X) * (x - E_X) * P[x - 1]
print("Variance:", Var_X)

SD_X = math.sqrt(Var_X)
print("Standard deviation:", SD_X)

print()

print("1d.")
CDF_X = sum(P[3:])
print(CDF_X)
