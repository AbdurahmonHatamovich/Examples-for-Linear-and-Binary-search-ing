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

arr = [1, 3, 5, 7, 9]
target = int(input("Kiriting: "))
result = binary_search(arr, target)
print(result)