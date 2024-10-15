dec = int(input("Please type in a decimal number to convert: "))
binary = []
while dec>0:
    binary.insert(0,dec%2)
    dec = int(dec/2)
print(''.join([str(x) for x in binary]))
