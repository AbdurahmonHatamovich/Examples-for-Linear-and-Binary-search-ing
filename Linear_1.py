#Royhatdagi raqamni qidirish

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f" Kiritilgan raqam mavjud"
    return f"Kiritilga raqam mavjud emas"

arr = [4, 2, 7, 9, 1]
target = int(input("Raqam kiriting: "))
result = linear_search(arr, target)
print(result)