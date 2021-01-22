import sys

sys.stdin = open("10912.외로운문자.txt", 'r')

for tc in range(1, int(input())+1):
    S = list(input())
    S.sort()

    stack = []
    for i in S:
        if stack and stack[-1] == i:
            stack.pop()
        else:
            stack.append(i)
    
    if stack:
        print(f"#{tc} {''.join(stack)}")
    else:
        print(f"#{tc} Good")