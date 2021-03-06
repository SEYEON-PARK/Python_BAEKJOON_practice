'''
자연수 A, B가 주어지면 A+B를 구하는 프로그램을 작성하시오.

자연수 A, B (0 < A, B ≤ 10)가 첫 번째 줄에 주어진다. 단, 두 수의 사이에는 공백이 주어지지 않는다. 두 수의 앞에 불필요한 0이 붙는 경우는 없다.

첫 번째 줄에 A+B의 값을 출력한다.
'''

n=int(input()) # 사용자로부터 정수 입력받기
a=n # a에 n의 값 대입하기
b=n # b에 n의 값 대입하기

if len(str(n)) >= 3: # 만약, 정수 n을 문자열로 바꾼 것의 길이가 3보다 크거나 같으면
    if(n//10==10): # 만약, n//10의 결괏값이 10과 같다면
        a%=100 # a에 a%100 값 대입하기
        b//=10 # b에 b//10 값 대입하기
        print(a+b) # 결과 출력하기
    else: # 만약, n//10의 결괏값이 10과 같지 않다면
        a%=100 # a에 a%100 값 대입하기
        b//=100 # b에 b//100 값 대입하기
        print(a+b) # 결과 출력하기
    
else: # 정수 n을 문자열로 바꾼 것의 길이가 3보다 크거나 같지 않으면(작다면)
    a%=10 # a에 a%10 값 대입하기
    b//=10 # b에 b//10 값 대입하기
    print(a+b) # 결과 출력하기
