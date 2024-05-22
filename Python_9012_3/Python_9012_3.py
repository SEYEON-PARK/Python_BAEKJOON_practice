'''
괄호 문자열(Parenthesis String, PS)은 두 개의 괄호 기호인 ‘(’ 와 ‘)’ 만으로 구성되어 있는 문자열이다.
그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다. 한 쌍의 괄호 기호로 된 “( )” 문자열은 기본 VPS 이라고 부른다.
만일 x 가 VPS 라면 이것을 하나의 괄호에 넣은 새로운 문자열 “(x)”도 VPS 가 된다. 그리고 두 VPS x 와 y를 접합(concatenation)시킨 새로운 문자열 xy도 VPS 가 된다.
예를 들어 “(())()”와 “((()))” 는 VPS 이지만 “(()(”, “(())()))” , 그리고 “(()” 는 모두 VPS 가 아닌 문자열이다. 
여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다. 

입력 데이터는 표준 입력을 사용한다. 입력은 T개의 테스트 데이터로 주어진다. 입력의 첫 번째 줄에는 입력 데이터의 수를 나타내는 정수 T가 주어진다.
각 테스트 데이터의 첫째 줄에는 괄호 문자열이 한 줄에 주어진다. 하나의 괄호 문자열의 길이는 2 이상 50 이하이다. 

출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다. 
'''

import sys; # 표준 입출력을 사용하기 위해

number = int(sys.stdin.readline().rstrip()) # 사용자로부터 정수 입력받기

for i in range(number): # number번 반복
    brackets = sys.stdin.readline().rstrip() # 사용자로부터 문자열 입력받기
    openBracket = 0 # 여는 괄호의 개수를 저장할 변수 openBracket 선언 및 초기화
    closeBracket = 0 # 닫는 괄호의 개수를 저장할 변수 openBracket 선언 및 초기화
    count = 0 # 반복 횟수를 저장할 변수 count 선언 및 초기화
    
    for j in range(len(brackets)): # 0부터 문자열 brackets의 길이보다 작을 때까지 1씩 증가시킨 값을 j에 대입하며 반복 
        if(brackets[j] == '('): # 만약, brackets[j]가 '('와 같다면
            openBracket += 1 # openBracket에 1 더하기
        elif(brackets[j] == ')'): # 만약 brackets[j]가 '('와 같지 않고, ')'와 같다면
            if(openBracket > closeBracket): # 만약, openBracket이 closeBracket보다 크다면(여는 괄호가 먼저 나왔어야 함)
                closeBracket += 1 # closeBracket에 1 더하기
            else: # openBracket이 closeBracket보다 크지 않다면(작거나 같다면)
                sys.stdout.write("NO\n") # "NO\n" 출력하기
                break # 가장 가까운 반복문 빠져 나가기
        count += 1 # count에 1 더하기
                
    if(openBracket == closeBracket and count == len(brackets)): # 만약 openBracket과 closeBracket이 같고, count와 문자열 brackets의 길이가 같다면
        sys.stdout.write("YES\n") # "YES\n" 출력하기
    elif(openBracket > closeBracket): # 위의 조건과 안 맞고, openBracket이 closeBracket보다 크다면(여는 괄호가 더 많은 상황)
        sys.stdout.write("NO\n") # "NO\n" 출력하기
