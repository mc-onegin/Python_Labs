s = input()
s1 = ''
count = 1
for i in range(len(s)):
    if i + 1 == len(s) or s[i] != s[i+1]:
        s1 += (s[i])
        if count > 1:
            s1 += str(count)
        count = 1
    else:
        count += 1
print(s1)









