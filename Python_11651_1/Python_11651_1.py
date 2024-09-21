'''
2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

첫째 줄에 점의 개수 N (1 ≤ N ≤ 100,000)이 주어진다. 둘째 줄부터 N개의 줄에는 i번점의 위치 xi와 yi가 주어진다.
(-100,000 ≤ xi, yi ≤ 100,000) 좌표는 항상 정수이고, 위치가 같은 두 점은 없다.

첫째 줄부터 N개의 줄에 점을 정렬한 결과를 출력한다.
'''

N = int(input()) # 사용자로부터 정수 입력받기
li = list() # 리스트 li 생성
for i in range(N): # i에 0부터 N이 되기 전까지 1씩 증가시킨 값을 대입하며 반복
    x, y = map(int, input().split()) # 사용자로부터 두 개의 정수(x좌표, y좌표) 입력받기
    li.append([x, y]) # li에 [x, y] 추가하기

li.sort(key = lambda a : (a[1], a[0])) # li를 y좌표 기준 오름차순 정렬, 같으면 x좌표 기준 오름차순 정렬

for a in li: # li에 있는 요소를 하나씩 a에 대입하며 반복
    print(a[0], a[1]) # 정렬한 결과 출력하기
