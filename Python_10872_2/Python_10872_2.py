'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

첫째 줄에 정수 N(0 ≤ N ≤ 12)이 주어진다.

첫째 줄에 N!을 출력한다.
'''

N=int(input())
result=1

for i in range(N, 0, -1):
    result*=i

print(result)
