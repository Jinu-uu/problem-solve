from sys import stdin
from collections import defaultdict

class HashDict:

    def __init__(self, size:int) -> None:
        self.size:int = size
        self.hash_dict:dict = defaultdict(str, '')
    
    def __len__(self) -> int:
        return self.size

    def add_item(self, key:str, value:str) -> None:
        self.hash_dict[key] = value

    def search_item(self, key) -> str:
        return self.hash_dict[key]

N, M = map(int, stdin.readline().split(' '))
hd = HashDict(N)

for _ in range(hd.__len__()):
    site, pw = map(str, stdin.readline().split(' '))
    hd.add_item(site.rstrip(), pw.rstrip())

for _ in range(M):
    find = str(stdin.readline()).rstrip()
    print(hd.search_item(find))
