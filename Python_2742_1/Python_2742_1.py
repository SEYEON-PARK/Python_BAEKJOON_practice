'''
자연수 N이 주어졌을 때, N부터 1까지 한 줄에 하나씩 출력하는 프로그램을 작성하시오.

첫째 줄에 100,000보다 작거나 같은 자연수 N이 주어진다.

첫째 줄부터 N번째 줄 까지 차례대로 출력한다.
'''

a=int(input()) # 사용자로부터 정수 입력받기
for i in range(a, 0, -1): # i에 a부터 0이 되기 전까지 1씩 감소시켜서 대입하며 반복
    print(i) # 결과 출력하기