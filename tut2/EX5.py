import sys

str = input("Please type in a string: ")
sub = input("Please type in a substring: ")
if len(str)<len(sub):
    print("Invalid parameter!")
    sys.exit()
lengthToCheck = len(sub)
result = []
for i in range(0, len(str)-len(sub)+1):
    addOrNot = False
    for j in range(0,lengthToCheck):
        if str[i + j]==sub[j]:
            addOrNot = True
        else:
            addOrNot = False
            continue
    if addOrNot:
        result.append(i)
print("All occurrences (indices) of the substring in the string are: ")
print(result)