# max_students, students = map(int, input().split())
#
# arr = {}
# result = {}
#
# for i in range(students):
#     arr[i] = input()
#
# for i in arr.keys():
#     if arr.get(i) in result.values():
#
#
#     result[i] = arr.get(i)
#
#
# #
# # n = 0
# # while n < max_students:
# #     print(arr[n])
# #     n += 1

n, size = map(int, input().split())

all = []

for i in range(size):
    all.append(input())

result = dict()
n = 0 # key : "42341234" value : 1
while len(result.keys()) < size:
    result[all[n]] = n
    if all[n] in result.keys():
        result.pop(all[n])
        result[all[n]] = n + 1
    n += 1

sorted_result = sorted(result.values())
for i in sorted_result:

