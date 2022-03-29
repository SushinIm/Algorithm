
#n(n+1)/2

import time

case = int(input())
result = []

times = time.time()

for c in range(case):
    route = int(input())
    sum_val = 0
    jump = 1
    for x in range(0, route, jump):
        sum_val += jump
        if sum_val >= route:
            if route != 1:
                jump -= 1
            break
        jump += 1
    result.append(jump)

for c in result:
    print(c)

print(time.time() - times)