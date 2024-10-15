bin = input("Please type in a binary number: ")
arr = list(bin)
result = 0
i = len(arr)-1
j = 0
while i>=0:
    if(arr[i]=='1'):
        result+=pow(2,j)
    j+=1
    i-=1
print(result)
