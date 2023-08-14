"""
옛날 옛적에 수학이 항상 큰 골칫거리였던 나라가 있었다. 이 나라의 국왕 김지민은 다음과 같은 문제를 내고 큰 상금을 걸었다.
길이가 N인 정수 배열 A와 B가 있다. 다음과 같이 함수 S를 정의하자.
   S = A[0] × B[0] + ... + A[N-1] × B[N-1]
S의 값을 가장 작게 만들기 위해 A의 수를 재배열하자. 단, B에 있는 수는 재배열하면 안 된다.
S의 최솟값을 출력하는 프로그램을 작성하시오.

첫째 줄에 N이 주어진다. 둘째 줄에는 A에 있는 N개의 수가 순서대로 주어지고, 셋째 줄에는 B에 있는 수가 순서대로 주어진다. 
N은 50보다 작거나 같은 자연수이고, A와 B의 각 원소는 100보다 작거나 같은 음이 아닌 정수이다.

첫째 줄에 S의 최솟값을 출력한다.
"""

N = int(input()) # 사용자로부터 정수 입력받기
A = list(map(int, input().split())) # 사용자로부터 문자열을 입력받아 공백을 기준으로 자른 뒤, 정수형으로 형변환하고 리스트 A에 저장하기
B = list(map(int, input().split())) # 사용자로부터 문자열을 입력받아 공백을 기준으로 자른 뒤, 정수형으로 형변환하고 리스트 B에 저장하기

A=sorted(A) # 리스트 A를 오름차순으로 정렬한 걸 A에 대입하기
B=sorted(B, reverse=True) # 리스트 B를 내림차순으로 정렬한 걸 B에 대입하기

sum=0 # 결과를 저장할 변수 sum 선언 및 초기화

for i in range(N): # 0부터 N이 되기 전까지 1씩 증가시킨 값을 i에 대입하며 반복
    sum+=A[i]*B[i] # sum에 sum+(A[i]*B[i])의 값 대입하기

print(sum) # 결과 출력하기
