"""
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
"""

N, K = map(int, input().split()) # 사용자로부터 두 개의 정수 입력받기(동전 종류 개수, 원하는 금액)
coin_type = list() # 동전의 종류를 저장할 리스트 coin_type 선언
coin_count = 0 # 필요한 동전의 개수를 저장할 변수 coin_count 선언 및 0으로 초기화

for i in range(N): # 동전 종류 개수만큼 반복하기
    coin = int(input()) # 사용자로부터 정수 입력받기(동전 종류)
    coin_type.append(coin) # coin_type 리스트에 추가하기
    
coin_type.sort(reverse=True) # coin_type 리스트를 내림차순으로 정렬하기

for coin in coin_type: # 리스트 coin_type에 있는 요소들을 하나씩 coin에 넣으며 반복
    coin_count += int(K / coin) # K(금액)를 coin으로 나눈 몫을 coin_count에 더하기
    K %= coin # K(금액)를 coin으로 나눈 나머지를 K에 저장하기
    
print(coin_count) # 결과(필요한 동전의 개수) 출력하기
