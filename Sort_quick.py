import random
import datetime
import prettytable                  # пакет для таблицы


def QuickSort(A, fst, lst):         # быстрая сортировка
    if fst >= lst:
        return

    #i, j = fst, lst
    pivot = A[fst]
    # pivot = A[random.randint(fst, lst)]
    first_bigger = fst+1
    while first_bigger <= lst:
        if A[first_bigger] >= pivot:
            break
        first_bigger += 1
    i = first_bigger+1
    while i <= lst:
        if A[i] < pivot:
            A[i], A[first_bigger] = A[first_bigger], A[i]
            first_bigger += 1
        i += 1

    last_smaller = first_bigger-1
    A[fst], A[last_smaller] = A[last_smaller], A[fst]
    QuickSort(A, fst, last_smaller-1)
    QuickSort(A, first_bigger, lst)

table = prettytable.PrettyTable(["Размер списка", "Время быстрой"])
x = []
y1 = []
y2 = []

for N in range(10, 21, 5):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random()*(max-min)+min)))

    B = A.copy()
    print(B)
    t1 = datetime.datetime.now()
    QuickSort(A, 0, len(A) - 1)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Быстрая сортировка   " + str(N) + "   заняла   " + str((t2-t1).total_seconds()) + "c")
    print(A)
    print("---")
    table.add_row([str(N), str((t2-t1).total_seconds())])

print(table)
