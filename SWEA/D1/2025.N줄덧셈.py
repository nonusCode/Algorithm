import sys

sys.stdin = open("2025.N줄덧셈.txt", 'r')

N = int(input())

res = 0
for i in range(1, N+1):
    res += i

print(res)