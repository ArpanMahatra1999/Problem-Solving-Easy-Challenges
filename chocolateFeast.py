n, c, m = 7, 3, 2
chocolates = [int(n / c)]
remainder = 0
for i in chocolates:
    wrappers = i + remainder
    wc = int(wrappers / m) * m
    chocolates.append(int(wrappers / m))
    if wc == 0:
        break
    remainder = wrappers - wc
print(sum(chocolates))
