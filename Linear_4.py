#Dictionaryda malum bir kalitni qidirish :
def linear_search(n, key):
    for k in n:
        if k == key:
            return True
    return False

dictionary = {'a': 1, 'b': 2, 'c': 3,'d': 4, 'e': 5, 'f': 6 }
key = input( "Keyni kiriting: ")
found = linear_search(dictionary, key)
print(found)