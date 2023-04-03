from sys import stdin

N = int(input()) - 1

if N <= 0: print(1)
else:
    moduler =int(1e9)+7
    result = 1
    A = 2
    while(N):
        if N & 1:
            result = result * A % moduler
        A = A * A % moduler
        N >>= 1


    print(result)