from itertools import combinations
test_case = int(input())
for t in range(test_case):
    temp_items = list()
    item_num = int(input())
    # 일단 튜플로 리스트에 저장
    for i in range(item_num):
        item_name, item_category = map(str, input().split())
        temp_items.append((item_category, item_name))

    # 이제 반복문을 돌면서 딕셔너리에 저장
    items = {item[0]: [] for item in temp_items}
    for item in temp_items:
        items[item[0]].append(item[1])
    #print(items)

    # 경우의 수 계산 = 각 카테고리별 아이템 수 + (각 아이템 수 전부 곱)
    item_key = list(items.keys())
    #for k in range(1, len(item_key)+1):
        #print(list(combinations(item_key, k)))
        #for j in combinations(item_key, k):  # j = item_category






    # each_category_item_num = 0
    # each_item_product = 1
    # if len(list(items.keys())) == 1:
    #     each_item_product = 0
    # for k in items.keys():
    #     each_category_item_num += len(items[k])
    #     each_item_product *= len(items[k])
    #
    # print(each_category_item_num + each_item_product)
#
# 1
# 3
# mask face
# sunglasses face
# makeup face

# 1
# 3
# hat headgear
# sunglasses eyewear
# turban headgear