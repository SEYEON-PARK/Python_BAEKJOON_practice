'''
N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 
마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.
N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

첫째 줄에 정수 N(1 ≤ N ≤ 500,000)이 주어진다.

첫째 줄에 남게 되는 카드의 번호를 출력한다.
'''

class Queue: # 큐 클래스 선언
    def __init__(self): # 생성자
        self.items = [] # 요소를 담을 리스트 self.items 선언
        self.firstIdx = 0 # 첫 번째 요소의 인덱스를 나타낼 self.firstIdx 선언 및 0으로 초기화
    
    def push(self, x): # 큐에 추가해주는 역할의 push() 메소드
        self.items.append(x) # 리스트 self.items의 맨 마지막에 x 추가
    
    def pop(self): # 큐의 맨 처음 요소를 삭제하고 반환해주는 역할의 pop() 메소드
        self.firstIdx += 1 # self.firstIdx에 1 더하기
        return self.items[self.firstIdx-1] # 원래 첫 번째 요소였던 거를 반환하기
    
    def size(self): # 큐의 사이즈를 반환해주는 size() 메소드
        return len(self.items) - self.firstIdx # (리스트 self.items의 길이) - (self.firstIdx)의 값 반환하기
    
    def oneLeft(self): # 하나가 남았을 때 사용하는 oneLeft() 메소드
        return self.pop() # 하나 반환하기


q=Queue()
N = int(input())
for i in range(1, N+1):
    q.push(i)

while q.size() > 1:
    q.pop()
    q.push(q.pop())

print(q.oneLeft())
