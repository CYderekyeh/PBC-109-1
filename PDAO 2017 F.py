n, m = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
prev = 1
for x in a:
    if (x < prev):
        ans += n
    ans += x-prev
    prev = x
print(ans)