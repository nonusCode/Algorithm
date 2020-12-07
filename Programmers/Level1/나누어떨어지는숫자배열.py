def solution(arr, divisor):
    res = []
    for i in arr:
        if i % divisor == 0:
            res.append(i)
        else:
            pass
    if len(res) == 0:
        res.append(-1)
    res.sort()

    return res

# 1
arr = [5, 9, 7, 10]
divisor = 5

# 2
# arr = [2, 36, 1, 3]
# divisor = 1

# 3
# arr = [3, 2, 6]
# divisor = 10

print(solution(arr, divisor))