from itertools import product

channel = int(input())
num_of_broken = int(input())
if num_of_broken == 0:
    alive_buttons = [i for i in range(10)]
    broken_buttons = []
else:
    broken_buttons = list(map(int, input().split()))
    alive_buttons = [i for i in range(10) if i not in broken_buttons]

'''
1. 반올림을 자릿수 -1 번쨰에서 한다 425 -> 400
2. 제일 큰 자릿수의 숫자가 고장난지 체크한다
-안 고장났을 경우 : 그 수로 조합을 돌린다
-고장났을 경우 : 
해당 숫자보다 작은 수를 찾고, 큰 수를 찾아서 조합을 돌린다
'''

# 시작점이 100이면 바로 끝
if channel == 100:
    print(0)
    exit()

# 모든 버튼이 고장나면 아래 로직을 수행할 필요 없이 바로 출력
if not alive_buttons:
    print(channel)
    exit()

# 고장난 버튼이 하나도 없는 경우도 아래 로직을 수행할 필요 없이 바로 출력
if not broken_buttons:
    print(len(str(channel)))
    exit()

round_index = -(len(str(channel)) - 1)
rounded = round(channel, round_index)


def find_near_digit(n):
    return min(alive_buttons, key=lambda x: abs(x-n))


# 첫 자리수가 고장난 버튼인지 아닌지 판단
if int(str(channel)[0]) not in alive_buttons:
    first_digit = find_near_digit(int(str(rounded)[0]))
else:
    first_digit = int(str(channel)[0])


result = []
# 남은 버튼으로 만들 수 있는 모든 경우의 수 만들기
digit = len(str(channel))  # 가장 첫쨰자리수를 뺀 나머지 자리의 수
for tup in product(alive_buttons, repeat=digit-1):  # (1, 1, 1, 1, 1) 이런 형태의 튜플로 저장되어 있음
    temp = ""
    #print(f'경우의 수 = {tup}')
    for i in tup:
        temp += str(i)
    case = str(first_digit) + temp
    gap = abs(channel - int(case))  # 가고자 하는 채널과 해당 케이스가 얼만큼 떨어져 있는지
    #print(f'케이스 : {case}, 거리차 : {gap}')
    result.append((gap, len(case), case))

for tup in product(alive_buttons, repeat=digit):
    temp = ""
    #print(f'경우의 수 = {tup}')
    for i in tup:
        temp += str(i)
    case = str(first_digit) + temp
    gap = abs(channel - int(case))  # 가고자 하는 채널과 해당 케이스가 얼만큼 떨어져 있는지
    #print(f'케이스 : {case}, 거리차 : {gap}')
    result.append((gap, len(case), case))

for _ in result:
    print(f'거리차 : {_[0]}, 자릿수 : {_[1]}, 케이스 : {_[2]}')

final_result, num_press, dummy = min(result)
print(final_result + num_press)
print(f'거리차 : {final_result}, 자릿수 : {num_press}, 케이스 : {dummy}')

# 9999
# 10
# 0 1 2 3 4 5 6 7 8 9