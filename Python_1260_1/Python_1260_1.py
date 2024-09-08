'''
그래프를 DFS로 탐색한 결과와 BFS로 탐색한 결과를 출력하는 프로그램을 작성하시오.
단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고, 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.

첫째 줄에 정점의 개수 N(1 ≤ N ≤ 1,000), 간선의 개수 M(1 ≤ M ≤ 10,000), 탐색을 시작할 정점의 번호 V가 주어진다.
다음 M개의 줄에는 간선이 연결하는 두 정점의 번호가 주어진다. 어떤 두 정점 사이에 여러 개의 간선이 있을 수 있다. 입력으로 주어지는 간선은 양방향이다.

첫째 줄에 DFS를 수행한 결과를, 그 다음 줄에는 BFS를 수행한 결과를 출력한다. V부터 방문된 점을 순서대로 출력하면 된다.
'''

from collections import deque # deque를 사용하기 위해

vertex = dict() # 정점을 저장해둘 딕셔너리 dict() 생성 
num_v, num_e, start_v = map(int, input().split()) # 사용자로부터 세 개의 정수 입력받아 각각 변수에 저장하기

# 정점의 개수만큼 키 생성하고, 빈 리스트와 연결해두기!
for i in range(num_v):
    vertex[i+1] = []

# 간선의 개수만큼 반복하며 서로 연결된 정점 표시해두기!
for i in range(num_e): 
    a, b = map(int, input().split())
    vertex[a].append(b)
    vertex[b].append(a)

# DFS
for i in vertex: # 딕셔너리 vertex 안의 키 값을 하나씩 i에 대입하며 반복
    vertex[i].sort(reverse=True) # 각 키에 연결된 리스트를 내림차순 정렬(DFS는 스택을 이용하므로 작은 수의 정점이 먼저 나가게 하기 위함)
    
visited = set() # 방문한 정점을 표시할 세트 visited 생성
future_visit = deque([start_v]) # 앞으로 방문할 정점을 저장할 deque future_visit을 생성하고, 시작 정점을 추가(추가할 때 리스트 형식'[]'가 반드시 있어야 함!) 

while future_visit: # 앞으로 방문할 정점이 남아있다면 계속 반복
    node = future_visit.pop() # 스택처럼 방문할 정점을 뒤에서 빼어 node에 저장
    
    if node not in visited: # 만약, node가 방문하지 않은 정점이라면
        print(node, end=' ') # 출력하기
        visited.add(node) # 방문했다고 추가하기
        future_visit.extend(vertex[node]) # 연결되어 있는 정점들 future_visit에 추가

print() # 한 줄 띄기

# BFS
for i in vertex: # 딕셔너리 vertex 안의 키 값을 하나씩 i에 대입하며 반복
    vertex[i].sort() # 각 키에 연결된 리스트를 오름차순 정렬(BFS는 큐를 이용하므로 작은 수의 정점이 먼저 나가게 하기 위함)

visited = set() # 방문한 정점을 표시할 세트 visited 생성
future_visit = deque([start_v]) # 앞으로 방문할 정점을 저장할 deque future_visit을 생성하고, 시작 정점을 추가(추가할 때 리스트 형식'[]'가 반드시 있어야 함!) 

while future_visit: # 앞으로 방문할 정점이 남아있다면 계속 반복
    node = future_visit.popleft() # 큐처럼 방문할 정점을 앞에서 빼어 node에 저장
    
    if node not in visited: # 만약, node가 방문하지 않은 정점이라면
        print(node, end=' ') # 출력하기
        visited.add(node) # 방문했다고 추가하기
        future_visit.extend(vertex[node]) # 연결되어 있는 정점들 future_visit에 추가
