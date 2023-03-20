from sys import stdin

class coor_sort:

    def __init__(self, size) -> None:
        self.size = size
        self.coor = []
        self.i = 0

    def add(self, x,y) -> None:
        self.coor.append([x,y])

    @property
    def sorting(self) -> None:
        self.coor.sort(key=lambda x: (x[0], x[1]))

    def __next__(self) -> None:
        if self.i<len(self.coor):
            temp = self.coor[self.i]
            self.i+=1
            return temp
        else:
            raise StopIteration

    def __iter__(self) -> None:
        return self


if __name__ == '__main__':
    N = int(stdin.readline())
    result = coor_sort(N)

    for _ in range(N):
        x,y = map(int, stdin.readline().split())
        result.add(x,y)

    result.sorting

    for x,y in result:
        print(x, y)
