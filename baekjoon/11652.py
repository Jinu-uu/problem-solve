from sys import stdin
from collections import defaultdict

class maxmode:
    def __init__(self) -> None:
        self.dict = defaultdict(int)

    def add_ele(self, number) -> None:
        self.dict[number]+=1
    
    @property
    def result(self) -> int:
        return sorted([[item[0], item[1]] for item in self.dict.items()], key=lambda x:(-x[1], x[0]))[0][0]

N = int(stdin.readline())
mm = maxmode()
for _ in range(N):
    k = int(stdin.readline())
    mm.add_ele(k)
print(mm.result)