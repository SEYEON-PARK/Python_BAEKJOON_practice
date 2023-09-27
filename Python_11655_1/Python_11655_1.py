'''
ROT13은 카이사르 암호의 일종으로 영어 알파벳을 13글자씩 밀어서 만든다.
예를 들어, "Baekjoon Online Judge"를 ROT13으로 암호화하면 "Onrxwbba Bayvar Whqtr"가 된다. 
ROT13으로 암호화한 내용을 원래 내용으로 바꾸려면 암호화한 문자열을 다시 ROT13하면 된다. 
앞에서 암호화한 문자열 "Onrxwbba Bayvar Whqtr"에 다시 ROT13을 적용하면 "Baekjoon Online Judge"가 된다.
ROT13은 알파벳 대문자와 소문자에만 적용할 수 있다. 알파벳이 아닌 글자는 원래 글자 그대로 남아 있어야 한다. 
예를 들어, "One is 1"을 ROT13으로 암호화하면 "Bar vf 1"이 된다.
문자열이 주어졌을 때, "ROT13"으로 암호화한 다음 출력하는 프로그램을 작성하시오.

첫째 줄에 알파벳 대문자, 소문자, 공백, 숫자로만 이루어진 문자열 S가 주어진다. S의 길이는 100을 넘지 않는다.

첫째 줄에 S를 ROT13으로 암호화한 내용을 출력한다.
'''

a=input() # 사용자로부터 문자열 입력받기
s="" # 빈 문자열 s 선언

for i in a: # 문자열 a의 요소들을 i에 대입하며 반복
    if(i.isupper()): # 만약, i가 영어 대문자라면
        i=ord(i)+13 # i에 (문자 i의 아스키 코드값) + 13을 대입
        if i>90: # 만약, i가 90보다 크다면(아스키 코드 'Z'를 넘어갔다!)
            i=i-90+64 # i에 i-90+64의 값 대입하기
        s+=chr(i) # i의 값에 맞는 아스키 코드를 문자열 s에 더하기
    elif(i.islower()): # 만약 i가 영어 대문자가 아니고, 영어 소문자라면
        i=ord(i)+13 # i에 (문자 i의 아스키 코드값) + 13을 대입
        if i>122: # 만약, i가 122보다 크다면(아스키 코드 'z'를 넘어갔다!)
            i=i-122+96 # i에 i-122+96의 값 대입하기
        s+=chr(i) # i의 값에 맞는 아스키 코드를 문자열 s에 더하기
    else: # i가 영어 대문자가 아니고, 영어 소문자도 아니라면
        s+=i # i를 문자열 s에 더하기
        
print(s) # 결과 출력하기
