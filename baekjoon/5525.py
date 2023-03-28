from sys import stdin

N = int(stdin.readline())
M = int(stdin.readline())
string = str(stdin.readline()).rstrip()
find_IO = 'IO'* N +'I'
len_find_IO = len(find_IO)
count = 0
for idx in range(len(string)):
    if len(string) < idx+len_find_IO: break
    if find_IO == string[idx:idx+len_find_IO]: count += 1

print(count)