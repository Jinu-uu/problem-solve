from sys import stdin
from collections import Counter
string = stdin.readline().strip()
result = Counter(string)[' ']
if result == 0 and len(string) == 0: print(0)
else: print(result+1)