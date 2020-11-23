import sys

sys.stdin = open("2063.중간값찾기.txt", 'r')

N = int(input())
arr = list(map(int, input().split()))
arr.sort()

print(arr[len(arr) // 2])