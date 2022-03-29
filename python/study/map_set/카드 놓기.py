from itertools import permutations
import sys

cards, pick = int(sys.stdin.readline()), int(sys.stdin.readline())
datas = [int(sys.stdin.readline()) for _ in range(cards)]

answer = []

for per in permutations(datas, pick):
    answer.append(''.join(map(str, per)))

print(len(set(answer)))