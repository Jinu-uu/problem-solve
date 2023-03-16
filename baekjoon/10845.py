from sys import stdin

class queueue:

    def __init__(self)->None:
        self.q = []

    def __len__(self)->int:     #size
        return self.q.__len__()
    
    def input(self, command:list)->None:
        if command.__len__() == 2: self.push(int(command[1]))
        elif command[0] == 'pop': print(self.pop())
        elif command[0] == 'size': print(self.__len__())
        elif command[0] == 'empty':print(self.empty())
        elif command[0] == 'front':print(self.front())
        elif command[0] == 'back': print(self.back())

    def push(self, num)->None:
        self.q.append(num)

    def pop(self)->int:
        if self.__len__() == 0:
            return -1
        else:
            return self.q.pop(0)

    def empty(self)->int:
        if self.__len__() == 0: return 1
        else: return 0

    def front(self)->int:
        if self.__len__() == 0: return -1
        else: return self.q[0]

    def back(self)->int:
        if self.__len__() == 0: return -1
        else: return self.q[self.__len__()-1]

N = int(stdin.readline())
q = queueue()
for _ in range(N):
    command = list(map(str, stdin.readline().strip().split(' ')))
    q.input(command)
