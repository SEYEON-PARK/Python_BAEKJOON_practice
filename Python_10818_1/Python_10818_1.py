'''
N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 
둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 
모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.

첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.
'''

a=int(input()) # 사용자로부터 정수 입력받기

num=list(map(int, input().split())) # 사용자가 입력하는 정수들을 공백을 기준으로 나눠서 리스트 num에 저장

up=num[0] # up에 num[0] 값 대입하기
down=num[0] # down에 num[0] 값 대입하기

for i in range(len(num)): # 0부터 리스트 num의 길이가 되기 전까지(리스트 num의 길이-1) 1씩 증가하여 i에 대입하며 반복
    if num[i]>up: # 만약 num[i]가 up보다 크다면
        up=num[i] # up에 num[i] 대입하기
    if num[i]<down: # 만약 num[i]가 down보다 작다면
        down=num[i] # down에 num[i] 대입하기
        
print(down, up) # 결과 출력하기
