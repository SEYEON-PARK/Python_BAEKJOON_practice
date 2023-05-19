'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

첫째 줄에 N!을 출력한다.
'''

def fac(n): # 함수 fac(n) 선언
    if n<=1: # 만약, n이 1보다 작거나 같다면
        return 1 # 1 반환하기
    return n*fac(n-1)

N=int(input())
print(fac(N))
