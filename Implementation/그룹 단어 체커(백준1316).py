import sys
input = sys.stdin.readline
n = int(input())


def group_word_checker(word):
    for i, char in enumerate(word):
        now_char = char
        if i < len(word) - 1:
            next_char = word[i + 1]
        else:
            break
        start = i
        while True:
            if now_char == next_char or i == len(word) - 1: break
            i += 1
            next_char = word[i]
        chunk = word[start:i + 1]
        for j in range(len(chunk) - 1):
            if chunk[j] != chunk[j + 1] and chunk[0] == chunk[-1]:
                return False
    return True


result = 0
for _ in range(n):
    word = input().rstrip()
    if group_word_checker(word):
        result += 1
print(result)






