N = 1000000
check= [0, 0] + [1]*(N-1)
res = []

for i in range(2, N+1):
    if check[i]:
        res.append(i)
    for j in range(2*i, N+1, i):
        check[j] = 0

print(*res, end=' ')