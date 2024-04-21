'''
정수 N이 주어졌을 때, 소인수분해하는 프로그램을 작성하시오.

첫째 줄에 정수 N (1 ≤ N ≤ 10,000,000)이 주어진다.

N의 소인수분해 결과를 한 줄에 하나씩 오름차순으로 출력한다. N이 1인 경우 아무것도 출력하지 않는다.
'''

N = int(input()) # 사용자로부터 정수 입력받기

while(N != 1): # N이 1이 아니라면 계속 반복
    for i in range(2, N+1): # 2부터 N+1보다 작을 때까지 1씩 증가시킨 값을 i에 대입하며 반복
        if(N % i == 0): # 만약, N % i의 값이 0과 같다면
            print(i) # i 출력하기
            N //= i # N에 N // i의 값 대입하기
            break # 가장 가까운 반복문 빠져 나가기
        elif(i == N-1): # 만약 N % i의 값이 0과 같지 않고, i가 N-1과 같다면
            print(N) # N 출력하기
            N //= i # N에 N // i의 값 대입하기
            break # 가장 가까운 반복문 빠져 나가기
