with open('input.txt') as file:
    numbers = file.read().split()
    numbers = list(map(int, numbers))
multi = 1
for i in range(len(numbers)):
    multi *= numbers[i]

with open('output.txt', 'w') as file:
    file.write(str(multi))
