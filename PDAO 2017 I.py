def addin3(n):
    if n <= 0:
        return [0]
    n3 = []
    while n > 0:
        remain = n % 3
        n3.append(remain)
        n //= 3
    l = len(n3)
    sm = []
    times = n3[0] + 1
    if n3[0] == 1:
        sm.append(1)
    else:
        sm.append(0)
    for i in range(1, len(n3)):
        digit = n3[i] * times
        digit %= 3
        sm.append(digit)
    return sm
a, b = map(int, input().split())
a3 = addin3(a-1)
print(a3)
b3 = addin3(b)
print(b3)
for i in range(len(a3)):
    b3[i] -= a3[i]
    if (b3[i] < 0):
        b3[i] += 3
b3.reverse()
res = 0
for x in b3:
    res *= 3
    res += x
print(res)
