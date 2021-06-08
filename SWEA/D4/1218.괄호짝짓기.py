import sys

sys.stdin = open("1218.괄호짝짓기.txt", 'r')

for tc in range(1, 11):
    N = int(input())
    arr = list(input())

    sol = dict()
    res = 1
    for i in arr:
        sol[i] = arr.count(i)
    
    if sol['['] == sol[']'] and sol['{'] == sol['}'] and sol['('] == sol[')'] and sol['<'] == sol['>']:
        res = 1
    else:
        res = 0

    print(f"#{tc} {res}")