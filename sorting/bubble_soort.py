<<<<<<< HEAD
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

elements = list(map(int, input('Enter values saperated by space: ').split()))
bubbleSort(elements)
print("Sorted Array is, ")
=======
def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

elements = list(map(int, input('Enter values saperated by space: ').split()))
bubbleSort(elements)
print("Sorted Array is, ")
>>>>>>> 1e4374c3a874f037ba1cfe876b6707251617a4f1
print(elements)