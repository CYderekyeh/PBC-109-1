n = int(input())
stk = []
max_stk = []
mx = 0
for i in range(n):
    s = str(input())
    if s[0] == '1':
        foo,v = map(int, s.split())
        stk.append(v)
        if v >= mx:
            max_stk.append(v)
            mx = v
    else:
        p = stk.pop()
        print(mx - p)
        if (p == mx):
            max_stk.pop()
            if not max_stk:
                mx = 0
            else:
                mx = max_stk[-1]