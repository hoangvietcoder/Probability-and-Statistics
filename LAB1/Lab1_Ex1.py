import itertools
A = (1, 2, 3, 4, 5)
k = 3

A_tmp = []
for i in A:
	A_tmp.append(str(i))

permute_k = list(itertools.permutations(A_tmp,k))
num_3_digit = []
for j in permute_k:
	num_3_digit.append(int(''.join(j)))
num_length = len(num_3_digit)

print(num_3_digit)
print(num_length)
