def solution(arr, divisior):
    answer = list(filter(lambda x: x % divisior == 0, sorted(arr)))
    if len(answer) <= 0:
        answer.append(-1)
    return answer