'''
itertools 조합을 써서 만든코드
(당연히 시간초과)
'''

# from itertools import combinations
# house, router = map(int, input().split())
# house_coord = list()
# for _ in range(house):
#     house_coord.append(int(input()))
#
# house_coord.sort()
#
# max_result = 0
# for case in combinations(house_coord, router):
#     #print(case)
#     min_gap = case[1] - case[0]
#     for i in range(len(case)-1):
#         min_gap = min(min_gap, case[i+1] - case[i])
#     #print(min_gap)
#     max_result = max(max_result, min_gap)
# print(max_result)


'''
이분탐색 활용 코드
'''

house, router = map(int, input().split())
house_coord = list()
for _ in range(house):
    house_coord.append(int(input()))

house_coord.sort()

start, end = 1, max(house_coord) - min(house_coord)

answer = 0
while start <= end:
    mid = (start + end) // 2

    count = 1  # 공유기의 개수
    current_house = house_coord[0]
    for i in range(1, house):
        if house_coord[i] - current_house >= mid:
            count += 1
            current_house = house_coord[i]

    if count >= router:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)