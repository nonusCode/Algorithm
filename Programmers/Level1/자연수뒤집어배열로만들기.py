def solution(n):
    n = list(str(n))
    res = []
    for i in range(len(n)):
        res.append(int(n.pop()))

    return res

# 1
n = 12345

print(solution(n))