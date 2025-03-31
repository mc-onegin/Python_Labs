def sort_dig(number):
    return ''.join(sorted(str(number)))


with open('input2.txt') as file:
    numbers = file.readlines()
    numbers = list(map(int, numbers))
srt = sorted(numbers, key=sort_dig)
with open('output2.txt', 'w') as file:
    for i in range(len(srt)):
        file.write(f"{str(srt[i])}\n")
