import sys

sys.stdin = open("1223.계산기2.txt", 'r')

def res():
    return eval(arr)

for tc in range(1, 11):
    N = int(input())
    arr = input()

    print(f"#{tc} {res()}")