def solution(numbers):
    res = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j:
                continue
            else:
                res.append(numbers[i] + numbers[j])
    
    res = sorted(list(set(res)))
    
    return res

# 1
numbers = [2, 1, 3, 4, 1]

# 2
# numbers = [5, 0, 2, 7]

print(solution(numbers))