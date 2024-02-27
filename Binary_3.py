

# Agar mavjud bo'lsa, x in arr indeksini qaytaradi, aks holda False
def binarySearch(arr, l, r, x):
    if r >= l:

        mid = l + (r - l) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            return binarySearch(arr, l, mid - 1, x)
        else:
            return binarySearch(arr, mid + 1, r, x)
    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = int(input("Son kiriting: "))

result = binarySearch(arr, 0, len(arr) - 1, x)

if result != -1:
    print(f"Element {result} chi indexda", )
else:
    print("Element bu arrayni ichida yoq")
