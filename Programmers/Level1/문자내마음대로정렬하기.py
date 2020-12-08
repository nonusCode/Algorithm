import operator

def solution(strings, n):
    sol = dict()
    res = []
    for i in strings:
        sol[(i[n], i)] = i
    
    sol = sorted(sol.items(), key=operator.itemgetter(0))
    
    for i in sol:
        res.append(i[1])
    
    return res

# 1
strings = ["sun", "bed", "car"]
n = 1

# 2
# strings = ["abce", "abcd", "cdx"]
# n = 2

print(solution(strings, n))