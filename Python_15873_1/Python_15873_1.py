'''
자연수 A, B가 주어지면 A+B를 구하는 프로그램을 작성하시오.

자연수 A, B (0 < A, B ≤ 10)가 첫 번째 줄에 주어진다. 단, 두 수의 사이에는 공백이 주어지지 않는다. 두 수의 앞에 불필요한 0이 붙는 경우는 없다.

첫 번째 줄에 A+B의 값을 출력한다.
'''

n=int(input())

if len(str(n)) >= 3:
    if(len(str(n))==4):
        a=n
        b=n
        a%=100
        b//=100
        print(a+b)
    elif(n//10==10):
        a=n
        b=n
        a%=100
        b//=10
        print(a+b)
    else:
        a=n
        b=n
        a%=100
        b//=100
        print(a+b)
    
else:
    a=n
    b=n
    a%=10
    b//=10
    print(a+b)
