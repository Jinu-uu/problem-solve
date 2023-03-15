class strepeat:
    def __init__(self, repeat: int, text:str):
        self.repeat = repeat
        self.text = text
    
    def repeatstr(self)->str:
        result = ''.join([self.text[x] for x in range(len(self.text)) for _ in range(self.repeat)])
        return result

T = int(input())

for x in range(T):
    R, S = input().split(' ')
    result = strepeat(int(R),S)
    print(result.repeatstr())