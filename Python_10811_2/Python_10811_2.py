'''
'''

N, M = map(int, input().split())
bag = list()

for i in range(N):
    bag.append(i+1)

for _ in range(M):
    a, b = map(int, input().split())
    bag[a-1:b] = bag[a-1:b][::-1]
    
for i in range(N):
    print(bag[i], end=" ")
