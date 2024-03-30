'''
문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오.
즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다. S에는 QR Code "alphanumeric" 문자만 들어있다.
QR Code "alphanumeric" 문자는 0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ\$%*+-./: 이다.

첫째 줄에 테스트 케이스의 개수 T(1 ≤ T ≤ 1,000)가 주어진다.
각 테스트 케이스는 반복 횟수 R(1 ≤ R ≤ 8), 문자열 S가 공백으로 구분되어 주어진다. S의 길이는 적어도 1이며, 20글자를 넘지 않는다. 

각 테스트 케이스에 대해 P를 출력한다.
'''

N = int(input()) # 사용자로부터 정수 입력받기

for i in range(N): # 0부터 N이 되기 전까지 1씩 증가시킨 값을 i에 대입하며 반복
    num, s = map(str, input().split()) # 사용자로부터 문자열 두 개를 공백을 기준으로 잘라 입력받기
    num = int(num) # 첫 번째로 입력받은 문자열을 정수로 형변환하기
    
    for j in range(len(s)): # 0부터 문자열 s의 길이보다 작을 때까지 1씩 증가시킨 값을 j에 대입하며 반복
        for k in range(num): # 0부터 num이 되기 전까지 1씩 증가시킨 값을 k에 대입하며 반복
            print(s[j], end="") # s[j] 출력하기
    
    print() # 한 줄 띄기
