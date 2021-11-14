N=int(input())
a=list()

for i in range(N):
    a.append(int(input()))

a.sort()

for i in range(N):
    print(a[i])
