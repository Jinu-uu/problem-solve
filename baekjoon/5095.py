from sys import stdin

class matrix:
    def __init__(self, A:list, B:int, number:int, moduler:int) -> None:
        self.mat:list = A
        self.sqr_num:int = B
        self.number:int = number
        self.moduler:int = moduler
        self.result:list = [[1 if i == j else 0 for i in range(number)]for j in range(number)]

    def __len__(self) -> tuple:
        return (len(self.mat), len(self.mat))   # mat is squre matrix
    
    @property
    def print(self) -> None:
        for i in range(self.number):
            for j in range(self.number):
                print(self.result[i][j], end=' ')
            print()

    def mat_mul(self, mat_a:list, mat_b:list) -> list:
        tmp = [[0] * (len(mat_a)) for _ in range(len(mat_b[0]))]
        for i in range(len(mat_a)):
            for j in range(len(mat_a[0])):
                for k in range(len(mat_b[0])):
                    tmp[i][k] += mat_a[i][j] * mat_b[j][k]
                    tmp[i][k] %= self.moduler
        return tmp
    
    @property
    def mat_sqr(self) -> None:
        while(self.sqr_num):
            if self.sqr_num & 1:
                self.result = self.mat_mul(self.result, self.mat)
            self.mat = self.mat_mul(self.mat, self.mat)
            self.sqr_num >>= 1
            

N, M, P = map(int, stdin.readline().split(' '))

A = []
for _ in range(N):
    A.append(list(map(int, stdin.readline().split(' '))))
_ = list(map(int, stdin.readline().split(' ')))
mat = matrix(A,P,N,M)
mat.mat_sqr
mat.print