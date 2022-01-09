# total_people[i] 를 넘겨주는 함수
def find_max_pick(arr):
    count = 1
    target = arr[0]
    for j in range(1,len(arr)):
        if target[0] < arr[j][0] and target[1] < arr[j][1]:
            continue
        else:
            target = arr[j]
            count += 1
    return count

total_case = int(input())
total_people = []
for i in range(total_case):
    num_of_people = int(input())
    people_arr = list()
    for j in range(num_of_people):
        doc_score, inter_score = map(int, input().split())
        arr = list()
        arr.append(doc_score)
        arr.append(inter_score)
        people_arr.append(arr)
    total_people.append(people_arr)

result = []
for i in range(len(total_people)):
    total_people[i].sort()
    count = find_max_pick(total_people[i])
    result.append(count)


print(" ".join(str(i) for i in result))

# 1
# 7
# 3 6
# 7 3
# 4 2
# 1 4
# 5 7
# 2 5
# 6 1


