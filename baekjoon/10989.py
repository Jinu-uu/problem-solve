from collections import defaultdict
N = int(input())

ddict = defaultdict(int)
for _ in range(N):
    ddict[int(input())] += 1

sorted_ddict = sorted(ddict.items(), key = lambda item: item[0])

for key, value in sorted_ddict:
    for x in range(value): print(key)