def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[-1][1]
    pivot_tuple = arr[-1]


    left = []
    right = []

    for x in arr[:-1]:
        if x[1] <= pivot:
            left.append(x)
        else:
            right.append(x)

    return quick_sort(left) + [pivot_tuple] + quick_sort(right)

students = [
    ("Andi", 78),
    ("Budi", 65),
    ("Citra", 85),
    ("Dewi", 72),
    ("Eka", 90)
]
print("Quick Sort Result:")
print(quick_sort(students))