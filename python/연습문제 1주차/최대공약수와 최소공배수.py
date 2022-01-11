def solution(n, m):
    answer = [0]
    big = n if n>m else m
    small = n if n<m else m
    for i in range(1, small+1):
        if small % i == 0 and big % i == 0:
            answer[0] = i
    answer.append(big*small/answer[0])
    return answer