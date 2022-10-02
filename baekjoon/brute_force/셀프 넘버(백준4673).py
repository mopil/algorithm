def d(n):
    result = n
    for i in list(str(n)):
        result += int(i)
    return result


max_range = 10004
not_self_numbers = []
for i in range(1, max_range):
    if d(i) > max_range:
        break
    else:
        not_self_numbers.append(d(i))
for i in range(1, max_range):
    if i not in not_self_numbers:
        print(i)
