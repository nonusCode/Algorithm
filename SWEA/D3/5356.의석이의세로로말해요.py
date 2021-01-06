import sys
from itertools import zip_longest

sys.stdin = open("5356.의석이의세로로말해요.txt", 'r')

for tc in range(1, int(input())+1):
    arr = [input() for _ in range(5)]
    
    res = zip_longest(*arr)
    print(f"#{tc}", end=' ')
    for i in res:
        print("".join(filter(None, i)), end='')
    print()