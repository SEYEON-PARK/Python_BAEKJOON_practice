'''
피보나치 수는 0과 1로 시작한다. 0번째 피보나치 수는 0이고, 1번째 피보나치 수는 1이다. 그 다음 2번째 부터는 바로 앞 두 피보나치 수의 합이 된다.
이를 식으로 써보면 Fn = Fn-1 + Fn-2 (n ≥ 2)가 된다.
n=17일때 까지 피보나치 수를 써보면 다음과 같다.
0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597
n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.

첫째 줄에 n이 주어진다. n은 90보다 작거나 같은 자연수이다.

첫째 줄에 n번째 피보나치 수를 출력한다.
'''

n = int(input()) # 사용자로부터 정수 입력받기
pibo = [0, 1] # 피보나치 수를 저장해둘 리스트 선언 및 초기화
count = 1 # 몇 번째 피보나치 수인지 저장해둘 변수 count 선언 및 초기화

while(True): # 무한 반복
    if(count == n): # 만약, count가 n과 같다면
        print(pibo[-1]) # 리스트 pibo의 마지막 요소 출력하기 
        break # 반복문 빠져나가기
    pibo.append(pibo[-1]+pibo[-2]) # 리스트 pibo에 다음 요소 추가하기
    count += 1 # count에 1 더하기