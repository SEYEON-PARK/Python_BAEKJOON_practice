"""
양수 A가 N의 진짜 약수가 되려면, N이 A의 배수이고, A가 1과 N이 아니어야 한다. 어떤 수 N의 진짜 약수가 모두 주어질 때, N을 구하는 프로그램을 작성하시오.

첫째 줄에 N의 진짜 약수의 개수가 주어진다. 이 개수는 50보다 작거나 같은 자연수이다. 
둘째 줄에는 N의 진짜 약수가 주어진다. 1,000,000보다 작거나 같고, 2보다 크거나 같은 자연수이고, 중복되지 않는다.

첫째 줄에 N을 출력한다. N은 항상 32비트 부호있는 정수로 표현할 수 있다.
"""

n=int(input()) # 사용자로부터 정수 입력받기
a=list(map(int, input().split())) # 사용자로부터 정수들을 입력받아서 공백을 기준으로 나눠 리스트 a에 저장하기
a.sort() # 리스트 a를 오름차순 정렬하기

result=a[0]*a[-1] # result에 a[0]*a[-1] 값 대입하기

print(result) # 결과 출력하기
