n = int(input())
time = []
for i in range (n):
    time.append(int(input()))
time.sort()
total = 300
ans_count = 0
time_count = 0
penalty = 0
for i in range (n):
    total -= time[i]
    if (total >= 0):
        ans_count += 1
        time_count += time[i]
        penalty += time_count
    else:
        break
print(ans_count, penalty)