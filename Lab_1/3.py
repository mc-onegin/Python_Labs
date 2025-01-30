def pascal(n):
    row = [1]
    for i in range(n):
        if i % 2 == 1 and n % 2 == 0:
            print(" ", end="", sep="")
        elif i % 2 == 0 and n % 2 == 1:
            print(" ", end="", sep="")
        print(*[" "]*((n - i)//2) + row, sep = " ")
        row = [sum(x) for x in zip([0]+row, row+[0])]


n = int(input())
pascal(n)