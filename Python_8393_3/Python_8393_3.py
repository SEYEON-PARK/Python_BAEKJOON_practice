"""
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

1부터 n까지 합을 출력한다.
"""

def s(n): # 함수 s(n) 정의
    sum=0 # sum에 0 대입하기
    for i in range(n, 0, -1): # i에 n부터 0이 되기 전까지(1까지) 1씩 감소하며 반복
        sum+=i # sum에 sum+i 대입하기
    return sum # sum을 반환하기

a=int(input())
result=s(a)
    
print(result)
