k = int(input())
a = list(map(int, input().split()))
y = [0]
for i in range (1, k+1):
    if a[i - 1] == i:
        take = 2
    else:
        take = y[i-1] - y[a[i-1]-1] + 2
    y.append(take + y[i-1])
print(y[k] % 1000000007)