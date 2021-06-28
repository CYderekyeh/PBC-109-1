n = int(input())
prev = -1
ans = n
for i in range(n):
    if (a[i] == prev):
        ans -= 1
    prev = a[i]
print(ans)