import sys

sys.stdin = open("5601.쥬스나누기.txt", 'r')

for tc in range(1, int(input())+1):
    N = str(input())

    res = ('1'+'/'+ N).split() * int(N)

    print(f"#{tc}", end=' ')
    print(*res)