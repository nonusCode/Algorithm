import sys

sys.stdin = open("1234.비밀번호.txt", 'r')

for tc in range(1, 11):
    N, S = map(str, input().split())
    S = list(S)

    stack = []
    for i in range(len(S)):
        stack.append(S[i])
        if len(stack) >= 2:
            if stack[-2] == stack[-1]:
                stack.pop()
                stack.pop()
    
    print(f"#{tc}", ''.join(stack))