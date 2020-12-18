def solution(arr):
    res = 0
    for i in str(arr):
        res += int(i)

    if arr % res == 0:
        return True
    else:
        return False

# 1
arr = 10

# 2
# arr = 12

# 3
# arr = 11

# 4
# arr = 13

print(solution(arr))