import sys

n, k = map(int, sys.stdin.readline().split())
ans = {}

for i in range(k):
    num = sys.stdin.readline().rstrip()
    ans[num] = i

for item in sorted(ans.items(), key=lambda x : x[1])[:n]:
    print(item[0])