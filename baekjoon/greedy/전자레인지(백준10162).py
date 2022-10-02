n = int(input())
times = {300: 0, 60: 0, 10: 0}
for t in times.keys():
    q = n // t
    n -= t * q
    times[t] += q

if n != 0:
    print(-1)
else:
    for _ in times.values():
        print(_, end=" ")