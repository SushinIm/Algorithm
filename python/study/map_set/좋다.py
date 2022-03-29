import sys

n = int(sys.stdin.readline())
nums = sorted(list(map(int, sys.stdin.readline().split())))
answer = 0

for _ in range(n):
    temp = nums[:_] + nums[_+1:]
    start, end = 0, n - 2
    while start < end:
        total = temp[start] + temp[end]
        if total == nums[_]:
            answer += 1
            break
        elif total < nums[_]:
            start += 1
        else:
            end -= 1

print(answer)