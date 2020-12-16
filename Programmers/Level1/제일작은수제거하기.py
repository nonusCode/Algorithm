def solution(arr):
    if len(arr) <= 1:
        arr.pop()
        arr.append(-1)
    else:
        arr.remove(min(arr))
    return arr

# 1
arr = [4, 3, 2, 1]

# 2
# arr = [10]

print(solution(arr))