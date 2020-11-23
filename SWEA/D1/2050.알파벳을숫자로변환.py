import sys

sys.stdin = open("2050.알파벳을숫자로변환.txt", 'r')

S = input()

for i in S:
    print(ord(i)-64, end=' ')