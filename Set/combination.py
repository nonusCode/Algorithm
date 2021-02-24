# Combination : 조합

def combination(idx):
    if idx == N:
        if sum(check) == R:
            for i in range(N):
                if check[i] == 1:
                    print(arr[i], end=' ')
            print()
        return
    check[idx] = 1
    combination(idx+1)
    check[idx] = 0
    combination(idx+1)

N = len(arr)
R = 3
check = [0] * N
combination(0)