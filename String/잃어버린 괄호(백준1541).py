a = input().split('-')
num = []
for i in a:
    cnt = 0
    s = i.split('+')
    for j in s:
        cnt += int(j)
    num.append(cnt)
n = num[0]
for i in range(1, len(num)):
    n -= num[i]
print(n)

# arr = "90+00009-00009+90"
# arr = arr.split('-')
# result = []
# for n in arr:
#     result += n.split('+')
#
# for k in result:

# arr = list(arr)
#
# flag = False
# for i in range(len(arr)):
#     if arr[i] == '-' and not flag:
#         arr.insert(i+1, "(")
#         flag = True
#         continue
#
#     if arr[i] == '-' and flag:
#         arr.insert(i, ")")
#         flag = False
#         continue
#
# open_num = arr.count("(")
# close_num = arr.count(")")
# gap = open_num - close_num
# for k in range(gap):
#     arr.append(")")
#
# arr = "".join(str(i) for i in arr)
# print(arr)
# print(eval(arr))