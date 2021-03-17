import sys

sys.stdin = open("1224.계산기3.txt", 'r')

def res():
    return eval(arr)

for tc in range(1, 11):
    N = int(input())
    arr = input()

    print(f"#{tc} {res()}")