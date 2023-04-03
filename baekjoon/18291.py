from sys import stdin

def conq_sqr(num, factor, moduler):
    result = 1
    while(factor):
        if factor & 1:
            result = result * num % moduler
        num = num * num % moduler
        factor >>= 1
    return result

T = int(input())
moduler = int(1e9)+7
for _ in range(T):
    N = int(input())
    if N <= 2: print(1)
    else: print(conq_sqr(2, N-2, moduler))
