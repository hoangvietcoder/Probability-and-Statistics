import itertools


def cross(A, B):
    return {a + b for a in A for b in B}


arcades = cross('A', '0123456789')
sports_games = cross('S', '01234')
collect = arcades | sports_games

combinations_collect = list(itertools.combinations(collect, 5))

cards_solution = list()
for s in combinations_collect:
    count_a = 0
    count_s_g = 0
    for i in s:
        if i.count('A') > 0:
            count_a += 1
        if i.count('S') > 0:
            count_s_g += 1
    if count_a == 3 and count_s_g == 2:
        cards_solution.append(s)
print(len(cards_solution))
