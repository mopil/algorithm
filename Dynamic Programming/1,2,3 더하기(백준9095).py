test_case = int(input())
arr = [int(input()) for _ in range(test_case)]
d = [0] * (max(arr) + 1)
d[0], d[1], d[2] = 1, 2, 4
for j in range(3, max(arr)+1):
    d[j] = d[j - 1] + d[j - 2] + d[j - 3]

for n in arr:
    print(d[n-1])

