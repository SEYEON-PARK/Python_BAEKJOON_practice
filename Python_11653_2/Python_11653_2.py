'''
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
'''

N = int(input())

while(N != 1):
    for i in range(2, N+1):
        if(N % i == 0):
            print(i)
            N //= i
            break
        elif(i == N-1):
            print(N)
            N //= i
            break
            
