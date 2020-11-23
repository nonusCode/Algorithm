import sys

sys.stdin = open("2043.서랍의비밀번호.txt", 'r')

P, K = map(int, input().split())

print(P-K + 1)