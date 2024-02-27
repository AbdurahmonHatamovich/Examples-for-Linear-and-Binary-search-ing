def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False

arr = [(1, 'apple'), (2, 'banana'), (3, 'orange'), (4, 'grape')]
target = (2, 'banana')
result = binary_search(arr, target)
print(result)