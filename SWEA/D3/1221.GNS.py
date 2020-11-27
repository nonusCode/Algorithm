import sys

sys.stdin = open("1221.GNS.txt", 'r')

for t in range(1, int(input())+1):
    tc, N = input().split()
    arr = list(map(str, input().split()))

    sol = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}
    for i in range(len(arr)):
        for k, v in sol.items():
            if arr[i] == v:
                arr[i] = k
    arr.sort()
    for i in range(len(arr)):
        for k, v in sol.items():
            if arr[i] == k:
                arr[i] = v

    print(tc)
    print(*arr)