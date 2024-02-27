#Satrlar royhatida satrni qidirish

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return f"Bunday malumot bor"
    return f"Bunday malumot yoq"

arr = ["apple", "banana", "grape", "orange"]
target = input("Kiriting: ")
result = linear_search(arr, target)
print(result)
