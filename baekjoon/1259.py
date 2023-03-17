from sys import stdin

class palindrome:

    def __init__(self, num) -> None:
        self.string:str = str(num)
    
    def deter(self) -> str:
        for idx in range((len(self.string)+1)//2):
            if self.string[idx] != self.string[-(idx+1)]:
                return 'no'
            
        return 'yes'
    

while(True):
    N = int(stdin.readline())
    if N == 0: break
    else:
        palin = palindrome(N)
        print(palin.deter())