s = int(input())
n = 0

candidate = [n for n in range(1, s//2)]
for num in candidate:
    if s - num <= 0:
        break
    else:
        s -= num
        n += 1

print(n)