n = int(input())
time = list(map(int,input().split()))

time = sorted(time)
result = 0
for i in range(0, len(time)):
    for j in range(0, i+1):
        result += time[j]
print(result)

