'''
N극 : 0
S극 : 1
방향 1 : 시계
방향 -1 : 반시계
톱니 상태는 12시 방향부터 시계방향으로 8방향이 주어짐
'''


def rotate_clockwise(target_gear):
    length = len(gears[target_gear-1])
    tmp = gears[target_gear-1][-1]
    for i in range(length-2, -1, -1):
        gears[target_gear-1][i+1] = gears[target_gear-1][i]
    gears[target_gear-1][0] = tmp


def rotate_anti_clockwise(target_gear):
    length = len(gears[target_gear-1])
    tmp = gears[target_gear-1][0]
    for i in range(length-2):
        gears[target_gear-1][i] = gears[target_gear-1][i+1]
    gears[target_gear-1][-1] = tmp


'''
1번 톱니의 2번 인덱스 <-> 2번 톱니의 6번 인덱스
2번 톱니의 2번 인덱스 <-> 3번 톱니의 6번 인덱스
3번 톱니의 2번 인덱스 <-> 4번 톱니의 6번 인덱스
'''

gears = [list(input()) for _ in range(4)]
rotate_num = int(input())
for _ in range(rotate_num):
    rotated = [False for _ in range(4)]
    target_gear, rotate = map(int, input().split())
    if rotate == 1: # 시계방향
        rotate_clockwise(target_gear)
    else:
        rotate_anti_clockwise(target_gear)
    rotated[target_gear-1] = True

    # 나머지 톱니들 회전 처리
    for j in [0, 1, 2]:
        if gears[j][2] != gears[j][6]:
            for i in [j, j+1]:
                if not rotated[i]:
                    if rotate == 1:  # 시계방향
                        rotate_anti_clockwise(i)
                    else:
                        rotate_clockwise(i)
                    rotated[i] = True
# 점수 계산
score = 0
if gears[0][0] == "1": score += 1
if gears[1][0] == "1": score += 2
if gears[2][0] == "1": score += 4
if gears[3][0] == "1": score += 8
print(score)








