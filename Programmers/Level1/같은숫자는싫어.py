def solution(arr):
    tmp = arr[0]
    res = [arr[0]]
    for i in arr:
        if i == tmp:
            pass
        else:
            res.append(i)
        tmp = i
        
    return res

# 1
arr = [1, 1, 3, 3, 0, 1, 1]

# 2
# arr = [4, 4, 4, 3, 3]

print(solution(arr))