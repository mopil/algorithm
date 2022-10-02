import heapq
num_card, max_merge = map(int, input().split())
cards = list(map(int, input().split()))

heapq.heapify(cards)
for _ in range(max_merge):
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)
    heapq.heappush(cards, a + b)
    heapq.heappush(cards, a + b)
print(sum(cards))
