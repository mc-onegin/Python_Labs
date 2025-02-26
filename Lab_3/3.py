sp = [str(s) for s in input().split()]
ch = {}
for char in sp:
    if char in ch:
        ch[char] += 1
    else:
        ch[char] = 1
print(*ch.values())