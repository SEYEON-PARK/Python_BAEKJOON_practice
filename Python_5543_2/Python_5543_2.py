'''
상근날드에서 가장 잘 팔리는 메뉴는 세트 메뉴이다. 주문할 때, 자신이 원하는 햄버거와 음료를 하나씩 골라, 세트로 구매하면, 가격의 합계에서 50원을 뺀 가격이 세트 메뉴의 가격이 된다.
햄버거는 총 3종류 상덕버거, 중덕버거, 하덕버거가 있고, 음료는 콜라와 사이다 두 종류가 있다.
햄버거와 음료의 가격이 주어졌을 때, 가장 싼 세트 메뉴의 가격을 출력하는 프로그램을 작성하시오.

입력은 총 다섯 줄이다. 첫째 줄에는 상덕버거, 둘째 줄에는 중덕버거, 셋째 줄에는 하덕버거의 가격이 주어진다.
넷째 줄에는 콜라의 가격, 다섯째 줄에는 사이다의 가격이 주어진다. 모든 가격은 100원 이상, 2000원 이하이다.

첫째 줄에 가장 싼 세트 메뉴의 가격을 출력한다.
'''

min_hamburger = 2000 # 가장 싼 햄버거의 가격을 저장할 변수 min_hamburger 선언 및 최댓값 대입해두기
min_beverage = 2000 # 가장 싼 음료의 가격을 저장할 변수 min_beverage 선언 및 최댓값 대입해두기

for _ in range(3): # 3번 반복
    hamburger = int(input()) # 사용자로부터 정수(햄버거 가격) 입력받기
    if(hamburger < min_hamburger): # 만약, hamburger(입력받은 정수)가 min_hamburger보다 작다면
        min_hamburger = hamburger # min_hamburger에 hamburger의 값 대입하기

for _ in range(2): # 2번 반복
    beverage = int(input()) # 사용자로부터 정수(음료 가격) 입력받기
    if(beverage < min_beverage): # 만약, beverage(입력받은 정수)가 min_beverage보다 작다면
        min_beverage = beverage # min_beverage에 beverage의 값 대입하기

print(min_hamburger + min_beverage - 50) # 결과(가장 싼 세트 메뉴의 가격) 출력하기
