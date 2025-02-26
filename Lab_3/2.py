sp_1 = [int(el) for el in input().split()]
sp_2 = [int(el) for el in input().split()]
count = 0
new_sp = []
for i in range(len(sp_1)):
    for j in range(len(sp_2)):
        if sp_2[j] == sp_1[i]:
            new_sp.append((sp_2[j]))
print(len(set(new_sp)))
