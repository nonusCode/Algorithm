def solution(n, lost, reserve):
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for i in set_reserve:
        if i - 1 in set_lost:
            set_lost.remove(i - 1)
        elif i + 1 in set_lost:
            set_lost.remove(i + 1)

    res = n - len(set_lost)

    return res

# 1
n = 5
lost = [2, 4]
reserve = [1, 3, 5]

# 2
# n = 5
# lost = [2, 4]
# reserve = [3]

# 3
# n = 3
# lost = [3]
# reserve = [1]

print(solution(n, lost, reserve))