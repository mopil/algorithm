'''
N극 : 0
S극 : 1
방향 1 : 시계
방향 -1 : 반시계
톱니 상태는 12시 방향부터 시계방향으로 8방향이 주어짐
'''


def rotate(target, dir):
    if dir == -1: # 반시계
        temp = gears[target].pop(0)
        gears[target].append(temp)
    elif dir == 1: # 시계
        temp = gears[target].pop()
        gears[target].insert(0, temp)

'''
1번 톱니의 2번 인덱스 <-> 2번 톱니의 6번 인덱스
2번 톱니의 2번 인덱스 <-> 3번 톱니의 6번 인덱스
3번 톱니의 2번 인덱스 <-> 4번 톱니의 6번 인덱스
'''

gears = [list(input()) for _ in range(4)]
rotate_num = int(input())
for _ in range(rotate_num):
    will_rotate = [False for _ in range(4)]
    target_gear, direction = map(int, input().split())
    target_gear -= 1

    # 돌아갈 톱니들 먼저 체크
    for j in [0, 1, 2]:
        if gears[j][2] != gears[j+1][6]:
            will_rotate[j] = True
            will_rotate[j+1] = True

    rotate_logic = []
    if target_gear == 0:
        rotate_logic = [(1, direction * -1), (2, direction), (3, direction * -1)]
    elif target_gear == 1:
        rotate_logic = [(0, direction * -1), (2, direction * -1), (3, direction)]
    elif target_gear == 2:
        rotate_logic = [(1, direction * -1), (3, direction * -1), (0, direction)]
    elif target_gear == 3:
        rotate_logic = [(2, direction * -1), (1, direction), (0, direction * -1)]

    rotate(target_gear, direction)
    for rl in rotate_logic:
        gear, dir = rl[0], rl[1]
        if will_rotate[gear]:
            rotate(gear, dir)

# 점수 계산
score = 0
if gears[0][0] == "1": score += 1
if gears[1][0] == "1": score += 2
if gears[2][0] == "1": score += 4
if gears[3][0] == "1": score += 8
print(score)








