def find(a, n, summ):
    print("Triplets are: ")
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if (a[i] + a[j] + a[k]) == summ:
                    print(a[i], a[j], a[k])


array = [10, 20, 30, 9]
summ = 59

find(array, len(array), summ)