"""
예제를 보고 규칙을 유추한 뒤에 별을 찍어 보세요.

첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

첫째 줄부터 차례대로 별을 출력한다.
"""

N=int(input()) # 사용자로부터 정수 입력받기
a=1 # a에 1 대입하기

for i in range(2*N): # 0부터 2*N이 되기 전까지 1씩 증가한 값을 i에 대입하며 반복
    
    if (i%2==0): # 만약, i%2의 값이 0과 같다면
        a=1 # a에 1 대입하기
    else:
        a=0
        
    for j in range(N):
        if (a%2==1):
            print("*", end="")
            a=a+1
        else:
            print(" ", end="")
            a=a+1
            
    print()
