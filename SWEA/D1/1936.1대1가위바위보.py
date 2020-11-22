import sys

sys.stdin = open("1936.1대1가위바위보.txt", 'r')

A, B = map(int, input().split())

if A-B == 1 or A-B == -2:
    print('A')
else:
    print('B')