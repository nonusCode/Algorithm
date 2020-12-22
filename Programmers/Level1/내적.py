def solution(a, b):
    res = 0
    for i in range(len(a)):
        res += a[i] * b[i]
    
    return res

# 1
a = [1, 2, 3, 4]
b = [-3, -1, 0, 2]

# 2
# a = [-1, 0, 1]
# b = [1, 0, -1]

print(solution(a, b))