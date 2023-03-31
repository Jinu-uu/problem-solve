from sys import stdin

A,B,C = map(int, stdin.readline().split(' '))

result = 1
while(B):
    if B & 1:
        result = result * A % C
    A = A * A % C
    B >>= 1
print(result)
