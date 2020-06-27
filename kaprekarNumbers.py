p, q = 400, 700
for i in range(p, q + 1):
    l = (list(str(pow(i, 2))))
    if len(l) == 1:
        if i == pow(i, 2):
            print(i, end=' ')
    else:
        first, second = [], []
        for j in range(0, int(len(l) / 2)):
            first.append(l[j])
        for k in range(int(len(l) / 2), len(l)):
            second.append(l[k])
        if (int(''.join(first)) + int(''.join(second))) == i:
            print(i, end=' ')
