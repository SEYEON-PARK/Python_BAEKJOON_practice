"""
준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 주어진다. (1 ≤ N ≤ 10, 1 ≤ K ≤ 100,000,000)
둘째 줄부터 N개의 줄에 동전의 가치 Ai가 오름차순으로 주어진다. (1 ≤ Ai ≤ 1,000,000, A1 = 1, i ≥ 2인 경우에 Ai는 Ai-1의 배수)

첫째 줄에 K원을 만드는데 필요한 동전 개수의 최솟값을 출력한다.
"""

N, K = map(int, input().split())
coin_type = list()
coin_count = 0

for i in range(N):
    coin = int(input())
    coin_type.append(coin)
    
coin_type.sort(reverse=True)

for coin in coin_type:
    coin_count += int(K / coin)
    K %= coin
    
print(coin_count)
