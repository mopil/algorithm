a, b, c, m = map(int, input().split())

time = 0
fatigue = 0
work = 0

while time < 24 and a <= m:
    if fatigue + a <= m:
        fatigue += a
        work += b
    else:
        if fatigue - c <= 0:
            fatigue = 0
        else:
            fatigue -= c
    time += 1

print(work)