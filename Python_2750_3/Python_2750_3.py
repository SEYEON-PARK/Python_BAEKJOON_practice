N=int(input())
a=list()

for i in range(N):
    a.append(int(input()))

b=sorted(a)

for i in range(N):
    print(b[i])
