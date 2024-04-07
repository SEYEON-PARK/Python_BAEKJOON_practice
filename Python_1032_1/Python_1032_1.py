'''
시작 -> 실행 -> cmd를 쳐보자. 검정 화면이 눈에 보인다. 여기서 dir이라고 치면 그 디렉토리에 있는 서브디렉토리와 파일이 모두 나온다.
이때 원하는 파일을 찾으려면 다음과 같이 하면 된다.
dir *.exe라고 치면 확장자가 exe인 파일이 다 나온다. "dir 패턴"과 같이 치면 그 패턴에 맞는 파일만 검색 결과로 나온다.
예를 들어, dir a?b.exe라고 검색하면 파일명의 첫 번째 글자가 a이고, 세 번째 글자가 b이고, 확장자가 exe인 것이 모두 나온다.
이때 두 번째 문자는 아무거나 나와도 된다. 예를 들어, acb.exe, aab.exe, apb.exe가 나온다.
이 문제는 검색 결과가 먼저 주어졌을 때, 패턴으로 뭘 쳐야 그 결과가 나오는지를 출력하는 문제이다.
패턴에는 알파벳과 "." 그리고 "?"만 넣을 수 있다. 가능하면 ?을 적게 써야 한다. 그 디렉토리에는 검색 결과에 나온 파일만 있다고 가정하고, 파일 이름의 길이는 모두 같다.

첫째 줄에 파일 이름의 개수 N이 주어진다. 둘째 줄부터 N개의 줄에는 파일 이름이 주어진다.
N은 50보다 작거나 같은 자연수이고 파일 이름의 길이는 모두 같고 길이는 최대 50이다. 파일이름은 알파벳 소문자와 '.' 로만 이루어져 있다.

첫째 줄에 패턴을 출력하면 된다.
'''

N = int(input()) # 사용자로부터 정수 입력받기
li = list() # 리스트 li 선언
result = list() # 리스트 result 선언

for i in range(N): # i에 0부터 N보다 작을 때까지 1씩 증가시킨 값을 대입하며 반복
    li.append(input()) # 사용자로부터 문자열을 입력받아 리스트 li에 추가하기
    
for i in range(len(li[0])): # i에 0부터 문자열 li[0]의 길이보다 작을 때까지 1씩 증가시킨 값을 대입하며 반복
    compareChar = li[0][i] # compareChar에 li[0][i]의 값 대입하기
    result.append(compareChar) # 리스트 result에 compareChar 추가하기
    for j in range(1, N): # j에 1부터 N보다 작을 때까지 1씩 증가시킨 값을 대입하며 반복
        if(compareChar != li[j][i]): # 만약, compareChar이 li[j][i]와 같지 않다면(다른 문자열의 같은 자리 비교!)
            result.pop() # 리스트 result의 마지막 요소 빼기
            result.append("?") # 리스트 result에 "?" 추가하기 
            break # 반복문 빠져 나오기

print(''.join(result)) # 리스트 result의 요소들을 ''(빈 문자열)로 연결하여 출력하기 
