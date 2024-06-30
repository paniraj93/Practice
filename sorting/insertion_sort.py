<<<<<<< HEAD
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = list(map(int, input('Enter values saperated by space: ').split()))
insertionSort(arr)
=======
def insertionSort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = list(map(int, input('Enter values saperated by space: ').split()))
insertionSort(arr)
>>>>>>> 1e4374c3a874f037ba1cfe876b6707251617a4f1
print("Sorted array is:", arr)