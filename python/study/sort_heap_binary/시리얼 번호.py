gaesu = int(input())
guitars = []

def compare(i, j):
    i_len = len(guitars[i])
    j_len = len(guitars[j])
    if i_len == j_len:
        i_sum = sum(map(int, filter(lambda ii : ii.isdigit(), guitars[i])))
        j_sum = sum(map(int, filter(lambda jj : jj.isdigit(), guitars[j])))
        if i_sum == j_sum:
            if guitars[i] > guitars[j]:
                return True
        else:
            if i_sum > j_sum:
                return True
    else:
        if i_len > j_len:
            return True
    return False

for i in range(gaesu):
    guitars.append(input())

for i in range(gaesu-1):
    for j in range(i+1, gaesu):
        if compare(i, j):
            guitars[i], guitars[j] = guitars[j], guitars[i]

for guitar in guitars:
    print(guitar)