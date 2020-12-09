def solution(s):
    sol = []
    for i in s:
        sol.append(i)

    sol = sorted(sol, reverse=True)
    res = "".join(sol)
    
    return res

# 1
s = "Zbcdefg"

print(solution(s))