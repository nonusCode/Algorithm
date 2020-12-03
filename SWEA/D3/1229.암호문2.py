import sys

sys.stdin = open("1229.암호문2.txt", 'r')

for tc in range(1, 11): 
    N = int(input())
    O = list(map(int, input().split()))
    C = int(input())
    I = list(map(str, input().split()))

    for i in range(len(I)):
        if I[i] == 'I':
            x = int(I[i+1])
            y = int(I[i+2])
            s = I[int(i+3):int(i+3)+y]
            for j in s:
                O.insert(x, j)
                x += 1
        elif I[i] == 'D':
            x = int(I[i+1])
            y = int(I[i+2])
            del O[x:x+y]
        if x == y:
            continue

    
    print(f"#{tc}", end=' ')
    print(*O[:10])