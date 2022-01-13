import itertools
import random


def cross(A, B):
    return {a + b for a in A for b in B}


novels = cross('N', '12345')
poems = cross('P', '123')
dictionaries = cross('D', '1')
books = list(novels | poems | dictionaries)


def simulator_a(n):
    count = 0
    for i in range(n):
        list_check = list()
        books_temp = books.copy()
        for j in range(3):
            get_book = books_temp[random.randint(0, len(books_temp) - 1)]
            books_temp.remove(get_book)
            list_check.append(get_book)
        for k in list_check:
            if 'D' in k:
                count += 1
                break
    return count / n


print("a.", simulator_a(100000))


def simulator_b(n):
    count = 0
    for i in range(n):
        list_check = list()
        books_temp = books.copy()
        for j in range(3):
            get_book = books_temp[random.randint(0, len(books_temp) - 1)]
            books_temp.remove(get_book)
            list_check.append(get_book)
        count_novel = 0
        count_poem = 0
        for k in list_check:
            if 'N' in k:
                count_novel += 1
            if 'P' in k:
                count_poem += 1
        if count_novel == 2 and count_poem == 1:
            count += 1
    return count / n


print("b.", simulator_b(100000))
