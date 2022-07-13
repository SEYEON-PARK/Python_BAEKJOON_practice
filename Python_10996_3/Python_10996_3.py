"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

첫째 줄부터 차례대로 별을 출력한다.
"""

N=int(input())
a=1

for i in range(2*N):
    
    if (i%2==0):
        a=1
    else:
        a=0
        
    for j in range(N):
        if (a%2==1):
            print("*", end="")
            a=a+1
        else:
            print(" ", end="")
            a=a+1
            
    print()
