sp = [int(el) for el in input().split()]
result = []
for i in range(1, len(sp)):
    if sp[i-1] < sp[i]:
        result.append(sp[i])
print(result)