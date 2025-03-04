def top_3_elem(s):
    ch = {}
    for i in s:
        digit = int(i)
        if digit in ch:
            ch[digit] += 1
        else:
            ch[digit] = 1
    sorted_ch = sorted(ch.items(), key=lambda item: item[1], reverse=True)
    print(dict(sorted_ch[:3]))


top_3_elem(input())

