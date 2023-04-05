'''
f_2  = [0, 1] [f1]
f_3  = [1, 1] [f2]    

'''
class fibo:
    def __init__(self, number:int) -> None:
        self.number:int = number
        self.base_matrix:list[list] = [[0,1],[1,1]]
        self.result:list[list] = [[0,1],[1,1]]
        self.moduler:int = int(1e9)+7
    
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
        while(self.number):
            if self.number & 1:
                self.result = self.mat_mul(self.result, self.base_matrix)
            self.base_matrix = self.mat_mul(self.base_matrix, self.base_matrix)
            self.number >>= 1
        return self.result[0][1]

N = int(input())
fibo_num = fibo(N-1)
print(fibo_num.mat_sqr*2)