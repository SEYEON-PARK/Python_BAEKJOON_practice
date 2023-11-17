'''
0보다 크거나 같은 정수 N이 주어진다. 이때, N!을 출력하는 프로그램을 작성하시오.

첫째 줄에 정수 N(0 ≤ N ≤ 20)이 주어진다.

첫째 줄에 N!을 출력한다.
'''

N=int(input()) # 사용자로부터 정수 입력받기
result=1 # 결과를 저장할 변수 result 선언 및 초기화

for i in range(2, N+1): # i에 2부터 N+1이 되기 전까지 1씩 증가시킨 값을 대입하며 반복
    result*=i # result에 result*i의 값 대입하기!
    
print(result)
