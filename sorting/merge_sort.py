def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = arr[:mid]
    print("left list",left)
    right = arr[mid:]
    print("right list",right)
    left = merge_sort(left)
    print("left",left)
    right = merge_sort(right)
    print("right",right)
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result

# Example usage:
arr = list(map(int, input('Enter values saperated by space: ').split()))
arr = merge_sort(arr)
print("Sorted array is:", arr)