"""
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
"""

N, K = map(int, input().split()) # 동전 종류 개수, 원하는 값 입력받기
coin_type = list() # 동전 종류 저장해둘 리스트 coin_type 생성
coin_count = 0 # 필요한 동전 개수 저장할 변수 coin_count 선언 및 초기화

# 동전 종류를 리스트 coin_type에 저장하기
for i in range(N): # 동전 종류 개수만큼 반복
    coin = int(input())
    coin_type.append(coin)

# 필요한 동전 개수 그리디 알고리즘으로 구하기
for coin in reversed(coin_type): # 리스트 coin_type을 반대로 하여 coin에 대입(오름차순으로 저장되어 있으므로 내림차순이 된다.)
    coin_count += K // coin # 몫으로 최대한 가능한 개수 구하기
    K %= coin # 나머지로 값 변경하기
    
print(coin_count) # 결과 출력하기
