n, m, k = map(int, input().split())
A = list(map(int, input().split()))
t = []
for i in range(m):
    t.append(list(map(int, input().split())))
t_cnt = [0] * m
for i in range(k):
    a, b = map(int, input().split())
    t_cnt[a-1] += 1
    if (b != m): 
        t_cnt[b] -= 1
add = [0] * n
sm = 0
for i in range(m):
    sm += t_cnt[i];
    l = t[i][0];r = t[i][1];v = t[i][2]
    add[l-1] += v * sm
    if (r != n):
        add[r] -= v*sm
sm = 0
print("Yes")
for i in range(n):
    sm += add[i]
    A[i] += sm
    if (i == n-1):
        print(A[i], end = "")
    else:
        print(A[i], end = " ")
