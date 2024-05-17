"""
알파벳 소문자로만 이루어진 단어가 주어진다. 이때, 이 단어가 팰린드롬인지 아닌지 확인하는 프로그램을 작성하시오.
팰린드롬이란 앞으로 읽을 때와 거꾸로 읽을 때 똑같은 단어를 말한다. 
level, noon은 팰린드롬이고, baekjoon, online, judge는 팰린드롬이 아니다.

첫째 줄에 단어가 주어진다. 단어의 길이는 1보다 크거나 같고, 100보다 작거나 같으며, 알파벳 소문자로만 이루어져 있다.

첫째 줄에 팰린드롬이면 1, 아니면 0을 출력한다.
"""

import sys; # sys.stdin.readline().rstrip()를 사용하기 위해

word = sys.stdin.readline().rstrip(); # 사용자로부터 문자열(단어) 입력받기
front = 0 # 맨 앞부터 탐색할 변수 front을 0으로 초기화
back = len(word)-1 # 맨 뒤부터 탐색할 변수 back을 len(word)-1로 초기화

while(front < ((len(word)-1) / 2)): # 만약, front가 ((len(word)-1) / 2)보다 작다면(front가 문자열 중간 전까지만 확인)
    if(word[front] != word[back]): # 만약, word[front]가 word[back]와 다르다면(팰린드롬이 아님)
        print('0') # '0' 출력하기
        sys.exit(0); # 프로그램 종료시키가!(Python에서는 프로그램을 sys.exit()으로 종료시킬 수 있다.)
    else: # word[front]가 word[back]와 같다면(팰린드롬일 수도 있음)
        front += 1 # front를 1 증가시키기
        back -= 1 # back을 1 감소시키기
        
print('1') # 팰린드롬이어서 반복문을 무사히 빠져 나왔다면 '1' 출력하기
