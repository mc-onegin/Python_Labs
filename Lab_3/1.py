sp = [int(el) for el in input().split()]
new_sp = sp
maxi = -10**10
mini = 10**10
for i in range(len(new_sp)):
    if new_sp[i] > maxi:
        maxi = new_sp[i]
        index_maxi = i
    if new_sp[i] < mini:
        mini = new_sp[i]
        index_mini = i
new_sp[index_mini] = maxi
new_sp[index_maxi] = mini
print(new_sp)


