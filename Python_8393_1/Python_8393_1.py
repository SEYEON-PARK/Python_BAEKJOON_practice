'''
n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.

첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다.

1부터 n까지 합을 출력한다.
'''

a=int(input()) # 사용자로부터 정수 입력받기
sum=0 # sum에 0 대입하기

for i in range(1, a+1):
    sum+=i
    
print(sum)

Python언어 BAEKJOON 8393번 문제 풀기!(1)
