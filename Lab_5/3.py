with open('input3.txt', encoding='utf-8') as file:
    children = []
    for line in file:
        surname, name, age_str = line.strip().split()
        age = int(age_str)
        children.append((surname, name, age))
old = max(children, key=lambda x: x[2])
young = min(children, key=lambda x: x[2])

with open('old.txt', 'w') as file:
    file.write(f"{old[0]} {old[1]} {old[2]}\n")
with open('young.txt', 'w') as file:
    file.write(f"{young[0]} {young[1]} {young[2]}\n")
