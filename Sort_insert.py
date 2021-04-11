import random
import datetime
import prettytable                  # пакет для таблицы


def insertsort(A):                  # сортировка пузырьком
    for i in range(len(A)):
        t = A[i]
        j = i
        for j in range(j, 0, -1):
            if t < A[j-1]:
                A[j] = A[j-1]
            else:
                A[j-1] = t




table = prettytable.PrettyTable(["Размер списка", "Время вставки"])
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
    insertsort(A)
    t2 = datetime.datetime.now()
    y1.append((t2-t1).total_seconds())
    print("Cортировка вставками  " + str(N) + "   заняла   " + str((t2-t1).total_seconds()) + "c")
    print(A)
    print("---")
    table.add_row([str(N), str((t2-t1).total_seconds())])

print(table)
