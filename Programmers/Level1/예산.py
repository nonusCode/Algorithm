def solution(d, budget):
    d.sort()
    res = 0
    for i in range(len(d)):
        if budget < d[i]:
            break
        budget -= d[i]
        res += 1

    return res

# 1
d = [1, 3, 2, 5, 4]
budget = 9

# 2
# d = [2, 2, 3, 3]
# budget = 10

print(solution(d, budget))