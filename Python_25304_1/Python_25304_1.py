'''
준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 
준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.
영수증에 적힌,
  -구매한 각 물건의 가격과 개수
  -구매한 물건들의 총 금액
을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

첫째 줄에는 영수증에 적힌 총 금액 X가 주어진다.
둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 N이 주어진다.
이후 N개의 줄에는 각 물건의 가격 a와 개수 b가 공백을 사이에 두고 주어진다.

구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.
'''

import sys # 표준 입출력을 사용하기 위해

totalPrice = int(sys.stdin.readline().rstrip()) # 사용자로부터 정수(영수증에 적힌 총 금액) 입력받기
num = int(sys.stdin.readline().rstrip()) # 사용자로부터 정수(영수증에 적힌 구매한 물건의 종류의 수) 입력받기
sum = 0 # 구매한 물건의 가격 계산한 값을 저장할 변수 선언 및 초기화

for i in range(num): # 0부터 num이 되기 전까지 1씩 증가시킨 값을 i에 대입하며 반복
    price, count = map(int, sys.stdin.readline().rstrip().split()) # 사용자로부터 두 개의 정수 입력받기
    sum += price * count # sum에 sum + price * count의 값 대입하기
    
if(totalPrice == sum): # 만약, totalPrice와 sum이 같다면
    print("Yes") # "Yes" 출력하기
else: # totalPrice와 sum이 같지 않다면
    print("No") # "No" 출력하기
