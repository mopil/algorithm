def solution(number, k):
    stack = []
    i = 0
    while i < len(number):
        if k > 0 and stack and stack[-1] < number[i]:
            stack.pop()
            k -= 1
            continue
        stack.append(number[i])
        i += 1
    return ''.join(stack[:len(stack) - k])