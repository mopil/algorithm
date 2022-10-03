def solution(new_id: str):
    # step 1
    new_id = list(new_id.lower())

    # step 2
    result = []
    for n in new_id:
        if ord('a') <= ord(n) <= ord('z') or ord('0') <= ord(n) <= ord('9') or n == '-' or n == '_' or n == '.':
            result.append(n)

    # step 3
    stack = [result[0]]
    i = 1
    while i < len(result):
        before = stack[-1]
        now = result[i]
        if before == now == '.':
            i += 1
            continue
        stack.append(result[i])
        i += 1
    result = stack
    # step4
    try:
        if result[0] == '.':
            result.pop(0)
        if result[-1] == '.':
            result.pop(-1)
    except:
        pass

    # step 5
    if not result:
        result.append('a')

    # step 6
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result.pop(-1)

    # step 7
    if len(result) <= 2:
        while len(result) < 3:
            result.append(result[-1])

    answer = ""
    for c in result:
        answer += c
    return answer

print(solution("z-+.^."))