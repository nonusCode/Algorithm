# Power Set : 모든 부분집합

def powerSet(idx):
    if idx == N:
        for i in range(N):
            if check[i]:
                print(arr[i],end=" ")
        print()
        return
    check[idx] = 1
    powerSet(idx+1)
    check[idx] = 0
    powerSet(idx+1)

N = len(arr)
check = [0] * N
powerSet(0)