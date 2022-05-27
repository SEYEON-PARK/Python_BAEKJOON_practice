'''
알파벳 소문자로만 이루어진 단어 S가 주어진다. 
각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

첫째 줄에 단어 S가 주어진다. 단어의 길이는 100을 넘지 않으며, 알파벳 소문자로만 이루어져 있다.

각각의 알파벳에 대해서, a가 처음 등장하는 위치, b가 처음 등장하는 위치, ... z가 처음 등장하는 위치를 공백으로 구분해서 출력한다.
만약, 어떤 알파벳이 단어에 포함되어 있지 않다면 -1을 출력한다. 단어의 첫 번째 글자는 0번째 위치이고, 두 번째 글자는 1번째 위치이다.
'''

from string import ascii_lowercase # 모듈 string에서 ascii_lowercase 가져오기

alphabet_list = ascii_lowercase # alphabet_list에 ascii_lowercase 대입하기

S=input() # 사용자로부터 문자열 입력받기

for i in alphabet_list: # i에 alphabet_list의 요소들의 한 개씩 대입하며 반복
    if i in S: # 만약, 문자열 S 안에 i가 있다면
        print(S.index(i), end=" ") # 문자열 S 안에 있는 i의 위치(인덱스 번호) 출력하기
    else:
        print(-1, end=' ')
        
