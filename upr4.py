string=input()
result=[]
for i in range(0, len(string), 2):
    result.append(string[i:i+2])
result=''.join(["".join(reversed(group)) for group in result])
print(result)
