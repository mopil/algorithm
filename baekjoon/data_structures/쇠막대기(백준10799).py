exp = list(input())

stack = []
result = 0

for i in range(len(exp)):
    if exp[i] == '(':
        stack.append('(')

    else:
        if exp[i-1] == '(':
            stack.pop()
            result += len(stack)
        else:
            stack.pop()
            result += 1
print(result)

