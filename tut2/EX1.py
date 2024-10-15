inp = input("Please type in a string: ")
upper = 0
lower = 0
otherChar = 0
for char in inp:
    if char.isalpha():
        if char.islower():
            lower+=1
        if char.isupper():
            upper+=1
    else:
        otherChar+=1

print("The number of uppercase letters is:", upper)
print("The number of lowercase letters is:",lower)
print("The number of other characters is: ", otherChar)