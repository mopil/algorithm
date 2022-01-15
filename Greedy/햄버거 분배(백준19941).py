N, K = map(int, input().split())
table = input()

count = 0
peoples = table.count('P')
checked = []
for i in range(len(table)):
    if table[i] == 'P':
        checked.append([i, table[i]])

def solution(table):
    global checked
    count = 0
    for i in range(len(table)):
        if table[i] == 'P' and [i, table[i]] in checked:
            start = i
            j = i
            try:
                while table[j] != 'H':
                    j += 1
            except:
                j = N - 1
            end = j
            gap = end - start
            if gap > K:
                count -= 1
                checked.remove([i, table[i]])
    return count

a = solution(table)
temp = list(table)
temp.reverse()
temp = "".join(temp)
b = solution(temp)

total = peoples + (a+b)
print(temp, checked)
print(total, peoples, a, b)

# 4 1
# HPHP