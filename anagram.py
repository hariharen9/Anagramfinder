x = input("enter the first word \n")
y = input("enter the second word \n")


def anagram(x, y):
    x = x.lower()
    y = y.lower()
    return sorted(x) == sorted(y)


result = anagram(x, y)
print(result)
