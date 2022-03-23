import itertools

def solution(numbers):
    template = []
    answer = []
    nums = []
    for i in range(1, len(numbers) + 1):
        template += list(map(''.join, itertools.permutations(list(numbers), i)))
    template += [n for n in numbers]
    answer = list(set(map(int,template)))
    nums = list(set(map(int,template)))

    for _ in nums:
        if _ < 2:
            answer.remove(_)
            continue
        for x in range(2, int(_**0.5)+1):
            if _ % x == 0:
                answer.remove(_)
                break

    return len(answer)