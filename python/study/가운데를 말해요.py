import heapq
import sys

shout = int(sys.stdin.readline())

big = []
small = []

for i in range(shout):
    num = int(sys.stdin.readline())
    if len(big) == len(small):
        heapq.heappush(small, -num)
    else:
        heapq.heappush(big, num)

    if big and small and -small[0] > big[0]:
        temp = heapq.heappop(small) * -1
        heapq.heappush(small, heapq.heappushpop(big, temp) * -1)

    print(-small[0])