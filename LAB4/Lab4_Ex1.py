import itertools

numbers = [0, 1, 2, 5, 6, 9]
permutations_numbers = list(itertools.permutations(numbers, 4))

even_solution = list()
for s in permutations_numbers:
    if s[0] != 0 and s[len(s) - 1] % 2 == 0:
        even_solution.append(s)

for s in even_solution:
    for i in s:
        print(i, end="")
    print(" ", end="")
print()
print(len(even_solution))
