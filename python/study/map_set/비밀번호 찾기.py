import sys
siteg, pwg = map(int, sys.stdin.readline().split())

pws = dict()

for i in range(siteg):
    site, pw = sys.stdin.readline().split()
    pws[site] = pw

for i in range(pwg):
    print(pws[input()])