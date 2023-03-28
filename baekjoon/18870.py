from sys import stdin
from collections import defaultdict

N = int(stdin.readline())
coor = defaultdict()
arr = list(map(int, stdin.readline().split(' ')))
for value in arr:
    coor[value] = 1
coor = dict(sorted(coor.items()))

for idx, key in enumerate(coor):
    coor[key] = idx

for value in arr:
    print(coor[value])