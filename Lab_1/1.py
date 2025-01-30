def f(a, b, c):
    if (a > b): [a, b] = [b, a]
    if (a > c): [a, c] = [c, a]
    if (b > c): [b, c] = [c, b]
    return [a, b, c]

a, b, c = map(int, (input().split()))
mas = f(a, b, c)
minimum, maximum = mas[0], mas[2]
print("min:", minimum, ("<" if minimum < maximum else "="), "max:", maximum)