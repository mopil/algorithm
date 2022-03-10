import sys
input = sys.stdin.readline

line = list(input().rstrip())
current_char = line[0]
result = []
tmp = current_char
if len(line) == 1:
    print(-1)
    exit()
for i in range(1, len(line)):
    now_char = line[i]
    if i >= len(line)-1:
        if line[-1] != '.':
            tmp += line[-1]
        result.append(tmp)
    elif current_char != now_char:
        current_char = now_char
        result.append(tmp)
        tmp = current_char
    else:
        tmp += now_char
print(result)
view = ""
for chunk in result:
    if "X" in chunk:
        a4 = len(chunk) // 4
        b2 = len(chunk) - a4*4
        if b2 % 2 != 0:
            print(-1)
            exit()
        view += "AAAA" * a4
        view += "B" * b2
    else:
        view += len(chunk) * "."
print(view)
