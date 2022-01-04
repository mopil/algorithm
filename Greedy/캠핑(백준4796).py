result = []
while True:
    stay, maxStay, totalVacation = map(int, input().split())
    if stay == 0 and maxStay == 0 and totalVacation == 0:
        break
    q = totalVacation // maxStay
    lastDays = totalVacation % maxStay
    if lastDays >= stay:
        lastDays = stay
    days = q * stay + lastDays
    result.append(days)

for i in range(len(result)):
    print(f"Case {i+1}: {result[i]}")
