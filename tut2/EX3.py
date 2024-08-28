inp = input("Please type in a full name: ")
inp = inp.lower()
chars = list(inp)
chars[0]=chars[0].upper()
for i in range(0,len(chars)):
    if i != len(chars):
        if chars[i]==" ":
            chars[i+1]=chars[i+1].upper()
print("Your name written correctly is:", "".join(chars))

