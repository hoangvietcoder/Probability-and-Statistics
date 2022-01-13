import random
import math


print("2a.")
x = [random.randint(0, 2) for i in range(10000)]
print(x)

print()

print("2b.")
X = set(x)
print(X)

print()

print("2c.")
PD = [x.count(i) / len(x) for i in X]
print(PD)

print()

print("2d.")

E_X = 0
for x in X:
    E_X += x * PD[x - 1]

print("Expectation:", E_X)

Var_X = 0
for x in X:
    Var_X += (x - E_X) * (x - E_X) * PD[x - 1]
print("Variance:", Var_X)

SD_X = math.sqrt(Var_X)
print("Standard deviation:", SD_X)

print()

print("2e.")
CDF_X = sum(PD[1:])
print(CDF_X)
