n, m, k = map(int, input().split())
a = list(map(int, input().split()))
add = [0]*n
t = []
for i in range(m):
    t.append(list(map(int, input().split())))
for i in range(k):
    ab = list(map(int, input().split()))
    for x in ab:
        x -= 1
        add[t[x][0]-1] += t[x][2]
        if (t[x][1] < n):
            add[t[x][1]] -= t[x][2]
print("Yes")
sum = 0
for i in range (n):
    sum += add[i]
    if (i != n-1):
        print(a[i]+sum, end = " ")
    else:
        print(a[i]+sum)


