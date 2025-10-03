N = int(input())
ochn = 0
zaochn = 0
for i in range(N):
    inf = input().split()
    if inf[-1] == 'True':
        ochn += 1
    else:
        zaochn += 1
print(f'out: {ochn} {zaochn}')
