def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        s = str(bin(arr1[i] | arr2[i]))[2:]
        if len(s) < n:
            s = "0"*(n-len(s)) + s
        s = s.replace("0", " ")
        s = s.replace("1", "#")
        answer.append(s)
    return answer