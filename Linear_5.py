#To'plamlar ro'yxatida ma'lum bir elementni qidirish:

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False

arr = [{1, 3, 2}, {7, 3, 1}, {3, 1, 9}]
target = input("Kiriting: ")
result = linear_search(arr, target)
print(result)
