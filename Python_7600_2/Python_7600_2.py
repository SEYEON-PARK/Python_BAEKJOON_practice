'''
"The quick brown fox jumped over the lazy dogs."
이 문장은 모든 알파벳이 적어도 한 번은 나오는 문장으로 유명하다. 즉 26개의 서로 다른 문자를 갖고 있는 것이다.
각 케이스마다 문장에서 공백, 숫자, 특수 문자를 제외하고 얼마나 다양한 알파벳이 나왔는지를 구하면 된다. 대소문자는 하나의 문자로 처리한다. ex) 'A' == 'a'

입력은 250자를 넘지 않는 문장이 주어진다.
각 문장은 적어도 하나의 공백이 아닌 문자를 포함한다. (알파벳이 아닐 수 있다)
마지막 줄에는 '#'이 주어진다.

각 줄마다 출몰한 알파벳의 개수를 출력하면 된다.
'''

while True: # 무한 반복
    s=input() # 사용자로부터 문자열 입력받기
    s=s.lower() # s에 s를 소문자로 바꾼 문자열을 저장
    
    if(s=='#'): # 만약, s가 '#'과 같다면
        break
    
    alpha=""
    count=0
    for i in s:
        if i.isalpha():
            if i in alpha:
                continue;
            count+=1
            alpha+=i
            
    print(count)
