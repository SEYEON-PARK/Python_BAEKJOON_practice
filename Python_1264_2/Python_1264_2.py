'''
영문 문장을 입력받아 모음의 개수를 세는 프로그램을 작성하시오. 모음은 'a', 'e', 'i', 'o', 'u'이며 대문자 또는 소문자이다.

입력은 여러 개의 테스트 케이스로 이루어져 있으며, 각 줄마다 영어 대소문자, ',', '.', '!', '?', 공백으로 이루어진 문장이 주어진다. 각 줄은 최대 255글자로 이루어져 있다.
입력의 끝에는 한 줄에 '#' 한 글자만이 주어진다.

각 줄마다 모음의 개수를 세서 출력한다.
'''

mo=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', "O", 'U'] # 영어 모음을 모아둔 리스트 선언

while(True): # 무한 반복
    s=input() # 사용자로부터 문자열 입력받기
    if(s=="#"): # 만약, s가 "#"과 같다면
        break # 반복문을 빠져 나가기
        
    count=0 # 변수 count 선언 및 초기화
    
    for i in s: # 문자열 s에 있는 문자들을 하나씩 i에 대입하며 반복
        if i in mo: # 만약, 문자 i가 리스트 mo 안에 있는 문자라면
            count+=1 # count에 1 더하기
    
    print(count) # 결과 출력하기
