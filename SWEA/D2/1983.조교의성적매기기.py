import sys

sys.stdin = open("1983.조교의성적매기기.txt", 'r')

for tc in range(1, int(input())+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    sol = ["A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if j == 0:
                arr[i][j] = arr[i][j] * 0.35
            elif j == 1:
                arr[i][j] = arr[i][j] * 0.45
            else:
                arr[i][j] = arr[i][j] * 0.2
        arr[i] = sum(arr[i])
    
    tmp = arr[K-1]
    arr.sort(reverse=True)
    res = arr.index(tmp) // (N//10)
    
    print(f"#{tc} {sol[res]}")