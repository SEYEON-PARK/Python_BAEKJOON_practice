'''
세준이는 피시방에서 아르바이트를 한다. 세준이의 피시방에는 1번부터 100번까지 컴퓨터가 있다.
들어오는 손님은 모두 자기가 앉고 싶은 자리에만 앉고싶어한다. 따라서 들어오면서 번호를 말한다. 
만약에 그 자리에 사람이 없으면 그 손님은 그 자리에 앉아서 컴퓨터를 할 수 있고, 사람이 있다면 거절당한다.
거절당하는 사람의 수를 출력하는 프로그램을 작성하시오. 
자리는 맨 처음에 모두 비어있고, 어떤 사람이 자리에 앉으면 자리를 비우는 일은 없다.

첫째 줄에 손님의 수 N이 주어진다. N은 100보다 작거나 같다. 
둘째 줄에 손님이 들어오는 순서대로 각 손님이 앉고 싶어하는 자리가 입력으로 주어진다.

첫째 줄에 거절당하는 사람의 수를 출력한다.
'''

num=int(input()) # 사용자로부터 정수 입력받기
rejectCount=0 # 거절 횟수 저장할 변수 선언 및 초기화
countingList=[0 for i in range(101)] # countingList의 요소를 101개 만들고 전부 0으로 초기화

li=list(map(int, input().split())) # 사용자로부터 입력받은 수를 리스트 li에 저장
for i in li: # 리스트 li에 있는 요소들을 하나씩 i에 대입하며 반복
    countingList[i]+=1 # countingList[i]에 countingList[i]+1의 값 대입하기
    if(countingList[i]>1): # 만약, countingList[i]의 값이 1보다 크다면
        rejectCount+=1 # rejectCount에 rejectCount+1의 값 대입하기

print(rejectCount) # 결과 출력하기
