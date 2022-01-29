def binary_search(arr, n):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == n:
            print(1, end=" ")
            return
        if arr[mid] > n:
            end = mid - 1
        else:
            start = mid + 1
    print(0, end=" ")


n = int(input())
have_card = sorted(list(map(int, input().split())))
m = int(input())
check_card = list(map(int, input().split()))

for check in check_card:
    binary_search(have_card, check)

