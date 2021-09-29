'''
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력은 여러 개의 테스트 케이스로 이루어져 있다.
각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
입력의 마지막에는 0 두 개가 들어온다.

각 테스트 케이스마다 A+B를 출력한다.
'''

while True: # 무한 반복
    a, b=map(int, input().split()) # 사용자로부터 두 개의 정수 입력받기
    if(a==0 and b==0): # 만약, a가 0이고 b도 0이면
        break # 가장 가까운 반복문을 빠져나간다.
    print(a+b)
