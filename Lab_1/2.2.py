flag = True
s = ''
n = int(input())
for i in range(n, 0, -1):
    for j in range(i, 1, -1):
        s += str(j)
    for k in range(1, i + 1):
        s += str(k)
    if flag:
        length = len(s)
        flag = False
    print(s.center(length))
    s = ''