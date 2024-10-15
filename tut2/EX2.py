inp = input("Please type in a string: ")
dict = {}
for char in inp:
    if char not in dict:
        dict[char] = 1
    else:
        dict[char] += 1
print(dict)