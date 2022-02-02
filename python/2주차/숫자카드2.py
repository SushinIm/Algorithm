import sys

m = int(input())
n = list(map(int, sys.stdin.readline().split()))
m2 = int(input())
n2 = list(map(int, sys.stdin.readline().split()))

cards = {}

answer = []

for i in n:
    if i in cards:
        cards[i] += 1
    else:
        cards[i] = 1

for i in n2:
    if i in cards:
        print(cards[i], end=' ')
    else:
        print(0, end=' ')