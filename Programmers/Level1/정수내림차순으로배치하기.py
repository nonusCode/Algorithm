def solution(n):
    res = int("".join(sorted(str(n), reverse=True)))
    
    return res

# 1
n = 118372

print(solution(n))