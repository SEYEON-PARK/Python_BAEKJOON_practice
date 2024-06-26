'''
정수를 저장하는 스택을 구현한 다음, 입력으로 주어지는 명령을 처리하는 프로그램을 작성하시오.
명령은 총 다섯 가지이다.
  push X: 정수 X를 스택에 넣는 연산이다.
  pop: 스택에서 가장 위에 있는 정수를 빼고, 그 수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.
  size: 스택에 들어있는 정수의 개수를 출력한다.
  empty: 스택이 비어있으면 1, 아니면 0을 출력한다.
  top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없는 경우에는 -1을 출력한다.

첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다.
주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.
'''

import sys; # sys.stdin.readline().rstrip()을 사용하기 위해

N = int(sys.stdin.readline().rstrip()) # 사용자로부터 정수 입력받기(input()보다 빠르다!)
stack = list() # 스택 역할을 할 리스트 stack 선언

for i in range(N): # i에 0부터 N이 되기 전까지 1씩 증가시킨 값을 대입하며 반복
    command = sys.stdin.readline().rstrip().split() # 사용자로부터 어떤 명령어를 실행할 것인지 입력받기
    if(command[0]=='push'): # 만약, 명령어가 'push'라면
        stack.append(command[1]) # stack의 끝에 원하는 요소 대입
    elif(command[0]=='pop'): # 만약, 명령어가 앞에서 검사한 게 아니고 'pop'이라면
        if(len(stack)!=0): # 만약, stack의 길이가 0이 아니라면
            print(stack.pop()) # stack의 마지막 요소 빼고 출력하기
        else: # stack의 길이가 0이라면
            print('-1') # '-1' 출력하기
    elif(command[0]=='size'): # 만약, 명령어가 앞에서 검사한 게 아니고 'size'라면
        print(len(stack)) # stack의 길이 출력하기
    elif(command[0]=='empty'): # 만약, 명령어가 앞에서 검사한 게 아니고 'empty'라면
        if(len(stack)!=0): # 만약, stack의 길이가 0이 아니라면
            print('0') # '0' 출력하기
        else: # stack의 길이가 0이라면
            print('1') # '1' 출력하기
    else: # 명령어가 앞에서 검사한 것들이 전부 아니라면
        if(len(stack)!=0): # 만약, stack의 길이가 0이 아니라면
            print(stack[-1]) # stack의 마지막 요소 출력하기
        else: # stack의 길이가 0이라면
            print('-1') # '-1' 출력하기
