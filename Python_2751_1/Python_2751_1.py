'''
N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

첫째 줄에 수의 개수 N(1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄부터 N개의 줄에는 수가 주어진다. 이 수는 절댓값이 1,000,000보다 작거나 같은 정수이다. 수는 중복되지 않는다.

첫째 줄부터 N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력한다.
'''

import sys # sys.stdin.readline()을 사용하기 위해

N = int(sys.stdin.readline()) # 사용자로부터 정수 입력받기
li = [] # 빈 리스트 li 생성

for _ in range(N): # N번 반복
    num = int(sys.stdin.readline()) # 사용자로부터 정수 입력받기(반복이 커지면 커질수록 input()은 오래 걸린다. 따라서 반복문 안에서 입력받을 때는 sys.stdin.readline()을 이용하자!)
    li.append(num) # 입력받은 정수를 리스트 li에 추가하기

li.sort() # 리스트 li 오름차순 정렬하기

for i in range(N): # i에 0부터 N보다 작을 때까지 1씩 증가시킨 값을 대입하며 반복
    print(li[i]) # li[i] 출력하기
