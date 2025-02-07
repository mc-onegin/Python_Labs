s = input()
s1 = ''
k = 0
while k < len(s):
    char = s[k]
    if k + 1 < len(s) and s[k + 1].isdigit():
        count = int(s[k+1])
        s1 += char * count
        k += 2
    else:
        s1 += char
        k += 1
print(s1)