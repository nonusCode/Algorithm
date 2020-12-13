def solution(s):
    s = s.split(' ')
    res = ""
    for i in range(len(s)):
        for j in range(len(s[i])):
            if j % 2 == 0:
                res += s[i][j].upper()
            else:
                res += s[i][j].lower()
        res += res.join(' ')
    
    return res[:-1]

# 1
s = "try hello world"

print(solution(s))