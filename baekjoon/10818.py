from sys import stdin

N = int(input())
numbers = list(map(int,stdin.readline().split(' ')))
print(min(numbers),max(numbers))