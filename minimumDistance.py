a = [3, 2, 1, 2, 3]
count = len(a)
for i in range(len(a) - 1):
    for j in range(i + 1, len(a)):
        if a[i] == a[j] and j - i < count:
            count = j - i
if count != len(a):
    print(count)
else:
    print(-1)
