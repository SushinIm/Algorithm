def solution(arr, commands):
    answer = []
    for i in commands:
        answer.append(sorted(arr[i[0]-1:i[1]])[i[2]-1])
    return answer