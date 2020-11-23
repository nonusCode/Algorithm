res = ['#', '+', '+', '+', '+']

print(''.join(map(str, res)))

for i in range(len(res)-1):
    res[i], res[i+1] = res[i+1], res[i]
    
    print(''.join(map(str, res)))