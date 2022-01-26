from itertools import permutations
import sys
input = sys.stdin.readline

n = int(input().rstrip())

for _ in range(n):
    word = input().rstrip()
    #l_word = sorted(list(word), reverse=True)
    l_word = list(word)

    index = 0
    flag = False
    for case in permutations(l_word, len(word)):  # ('h', 'e', 'l', 'l', 'o')

        if flag:
            target = case
            break

        temp = "".join(i for i in case)

        if temp == word:
            index += 1
            flag = True
            continue

        index += 1

    print("".join(i for i in target))


