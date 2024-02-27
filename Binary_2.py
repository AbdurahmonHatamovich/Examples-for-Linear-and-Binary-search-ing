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

arr = ['a', 'b', 'c', 'd', 'e', 'f']
target = input("Kiriting: ")
result = binary_search(arr, target)
print(result)