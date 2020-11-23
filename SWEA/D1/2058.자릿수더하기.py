import sys

sys.stdin = open("2058.자릿수더하기.txt", 'r')

N = input()

res = 0
for i in N:
    res += int(i)

print(res)