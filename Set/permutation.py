# Permutation : 순열

def permutation(idx):
    if idx >= N:
        print(arr)
        return
    for i in range(idx, N):
        arr[i], arr[idx] = arr[idx], arr[i]
        permutation(idx+1)
        arr[i], arr[idx] = arr[idx], arr[i]

N = len(arr)
permutation(0)