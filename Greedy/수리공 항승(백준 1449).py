
numOfLeak, maxTapeLength = map(int, input().split())
leaks = list(map(int, input().split()))
leaks = sorted(leaks)
startIndex = 0
endIndex = 1
count = 1
for i in range(len(leaks)):
    try:
        gap = leaks[endIndex] - leaks[startIndex]
        if maxTapeLength > gap:
            endIndex += 1
            continue
        else:
            startIndex = endIndex
            endIndex = startIndex + 1
            count += 1
    except:
        pass

print(count)


