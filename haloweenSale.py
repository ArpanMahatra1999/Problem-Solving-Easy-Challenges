p, d, s, m = 20, 3, 80, 6
arr = [0]
for i in range(p, m, -d):
    if sum(arr) >= s:
        break
    else:
        arr.append(i)
if sum(arr) < s:
    x = s - sum(arr)
    while x > -1:
        arr.append(m)
        x = x - m
print(len(arr) - 2)
