import random
import datetime
import prettytable                  # пакет для таблицы


def bubblesort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        for j in range(len(A)-1-i):
            if A[j] > A[j+1]:
                a = A[j]
                A[j] = A[j+1]
                A[j+1] = a


table = prettytable.PrettyTable(["Размер списка", "Время пузырька"])
x = []
y1 = []
y2 = []

for N in range(100, 201, 50):
    x.append(N)
    min = 1
    max = N
    A = []
    for i in range(N):
        A.append(int(round(random.random()*(max-min)+min)))

    B = A.copy()
    print(B)
    t1 = datetime.datetime.now()
    bubblesort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Пузырьковая сортировка   " + str(N) + "   заняла   " + str((t2-t1).total_seconds()) + "c")
    print(A)
    print("---")
    table.add_row([str(N), str((t2-t1).total_seconds())])

print(table)
