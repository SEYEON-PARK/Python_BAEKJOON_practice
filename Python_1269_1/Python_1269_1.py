'''
자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오.
두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.
예를 들어, A = { 1, 2, 4 } 이고, B = { 2, 3, 4, 5, 6 } 라고 할 때,  A-B = { 1 } 이고, B-A = { 3, 5, 6 } 이므로, 대칭 차집합의 원소의 개수는 1 + 3 = 4개이다.

첫째 줄에 집합 A의 원소의 개수와 집합 B의 원소의 개수가 빈 칸을 사이에 두고 주어진다.
둘째 줄에는 집합 A의 모든 원소가, 셋째 줄에는 집합 B의 모든 원소가 빈 칸을 사이에 두고 각각 주어진다.
각 집합의 원소의 개수는 200,000을 넘지 않으며, 모든 원소의 값은 100,000,000을 넘지 않는다.

첫째 줄에 대칭 차집합의 원소의 개수를 출력한다.
'''

import sys # 표준 입력을 사용하기 위해

A, B = map(int, sys.stdin.readline().rstrip().split()) # 사용자로부터 두 개의 정수 입력받기
numA = set(map(int, sys.stdin.readline().rstrip().split())) # 사용자로부터 입력받은 문자열을 공백을 기준으로 잘라 int형으로 형변환한 후, set에 저장하여 numA에 대입
numB = list(map(int, sys.stdin.readline().rstrip().split())) # 사용자로부터 입력받은 문자열을 공백을 기준으로 잘라 int형으로 형변환한 후, list에 저장하여 numB에 대입
result = A+B # result에 A+B의 값 대입하기

for i in range(B): # i에 0부터 B가 되기 전까지 1씩 증가시킨 값을 대입하며 반복
    if(numB[i] in numA): # 만약, numB[i]가 세트 numA 안에 있다면
        result -= 2 # result에 result-2의 값 대입하기

print(result) # 결과 출력하기!
