s = input()
s = s.replace(' ', '')
char_count = {}
for char in s:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

items = list(char_count.items())
items.sort(key=lambda item: item[1], reverse = True)
sorted_char = {item[0]: item[1] for item in items}
cnt = 3
for key, item in sorted_char.items():
    print(f"{key}: {item}")
    cnt -= 1
    if cnt == 0:
        exit()


