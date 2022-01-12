def solution(n):
    return n.replace(n[0:-4], "*" * len(n[0:-4]))