def solution(s):
    p = s.count('p')
    P = s.count('P')
    y = s.count('y')
    Y = s.count('Y')
    sol = (p + P) -  (y + Y)
    
    if sol:
        res = False
    else:
        res = True

    return res

# 1
s = "pPoooyY"

# 2
# s = "Pyy"

print(solution(s))