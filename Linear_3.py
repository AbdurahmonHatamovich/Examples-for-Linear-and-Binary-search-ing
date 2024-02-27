#Royhatdagi malumotni nechinchi indexdaligini topish

def linear_search(arr, substring):
    for i in range(len(arr)):
        if substring in arr[i]:
            return f"{i}chi indexda "
    return f"Kiritilgan malumotni royhatda yoq! BOSHQA MALUMOT KIRITING!!"

arr = ["pineaplle", "melon", "kiwi", "strawberry"]
substring = input("Malumot kiriting: ")
result = linear_search(arr, substring)
print(result)
