'''
여러 개의 쇠막대기를 레이저로 절단하려고 한다.
효율적인 작업을 위해서 쇠막대기를 아래에서 위로 겹쳐 놓고, 레이저를 위에서 수직으로 발사하여 쇠막대기들을 자른다. 쇠막대기와 레이저의 배치는 다음 조건을 만족한다.
- 쇠막대기는 자신보다 긴 쇠막대기 위에만 놓일 수 있다.
- 쇠막대기를 다른 쇠막대기 위에 놓는 경우 완전히 포함되도록 놓되, 끝점은 겹치지 않도록 놓는다.
- 각 쇠막대기를 자르는 레이저는 적어도 하나 존재한다.
- 레이저는 어떤 쇠막대기의 양 끝점과도 겹치지 않는다.
아래 그림은 위 조건을 만족하는 예를 보여준다. 수평으로 그려진 굵은 실선은 쇠막대기이고, 점은 레이저의 위치, 수직으로 그려진 점선 화살표는 레이저의 발사 방향이다.
(그림)
이러한 레이저와 쇠막대기의 배치는 다음과 같이 괄호를 이용하여 왼쪽부터 순서대로 표현할 수 있다.
레이저는 여는 괄호와 닫는 괄호의 인접한 쌍 ‘( ) ’ 으로 표현된다. 또한, 모든 ‘( ) ’는 반드시 레이저를 표현한다.
쇠막대기의 왼쪽 끝은 여는 괄호 ‘ ( ’ 로, 오른쪽 끝은 닫힌 괄호 ‘) ’ 로 표현된다.
위 예의 괄호 표현은 그림 위에 주어져 있다.
쇠막대기는 레이저에 의해 몇 개의 조각으로 잘려지는데, 위 예에서 가장 위에 있는 두 개의 쇠막대기는 각각 3개와 2개의 조각으로 잘려지고, 이와 같은 방식으로 주어진 쇠막대기들은 총 17개의 조각으로 잘려진다.
쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 주어졌을 때, 잘려진 쇠막대기 조각의 총 개수를 구하는 프로그램을 작성하시오.

한 줄에 쇠막대기와 레이저의 배치를 나타내는 괄호 표현이 공백없이 주어진다. 괄호 문자의 개수는 최대 100,000이다.

잘려진 조각의 총 개수를 나타내는 정수를 한 줄에 출력한다.
'''

stick = input() # 사용자로부터 괄호 문자열 입력받기
stack = list() # 스택 역할을 할 리스트 stack 생성

last = '' # 바로 이전 괄호를 저장할 변수
result = 0 # 결과를 저장할 변수

# 닫을 때 pop(), 열 때 push(), 레이저인가 아닌가, 막대기가 언제 끊기는가
for s in stick: # 괄호 문자열을 하나씩 s에 넣으며 반복
    if(s == '('): # 만약, s가 '('와 같다면
        stack.append(s) # stack에 s 저장하기
    elif(s == ')' and s != last): # 만약 앞의 조건 안 맞고, s가 ')'이고, s가 last와 다르다면(last는 '('임으로, 레이저일 때를 의미함)
        stack.pop() # stack의 마지막 요소 꺼내기
        result += len(stack) # result에 result + (stack의 길이)의 값 대입하기(잘린 막대기 수 더해서 저장)
    else: # 앞의 조건 다 안 맞으면(막대기가 닫힐 때)
        stack.pop() # stack의 마지막 요소 꺼내기
        result += 1 # result에 1 더하기(끊긴 막대기 조각 1 더하기)
    last = s # last에 s 대입하기(다음 반복을 위해 last를 현재 문자로 바꾸기)

print(result) # 결과(잘려진 조각의 총 개수) 출력하기
