from sys import stdin
N = int(stdin.readline())
houses = list(map(int, stdin.readline().split(' ')))
houses.sort()
print(houses[(len(houses)-1)//2])