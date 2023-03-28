from sys import stdin
from collections import defaultdict
from collections import OrderedDict


# a = list(OrderedDict({'k1': 1, 'k2': 2, 'k3': 3}))
# print(a, a[0])

N, M = map(int, stdin.readline().split(' '))
pokemon_hash = OrderedDict()

for idx in range(N):
    pokemon = str(stdin.readline()).rstrip()
    pokemon_hash[pokemon] = str(idx+1)

pokemon_list = list(pokemon_hash)

for _ in range(M):
    find = str(stdin.readline()).rstrip()
    try:
        find = int(find)
        print(pokemon_list[find-1])
    except ValueError:
        print(pokemon_hash[find])
    