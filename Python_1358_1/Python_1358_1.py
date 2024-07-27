'''
지난주에, 민식주식회사는 IIHF(International Ice Hockey Federation)로부터 긴급한 전화를 받았다.
IIHF는 같은 팀이 링크안에 너무 많으면 알람이 울리는 시스템을 설치해달라고 요청했다. 시스템은 다음과 같이 3개의 부분으로 이루어진다.
  - 디지털카메라가 링크의 사진을 매 1초마다 찍는다.
  - 디지털카메라가 찍은 사진에서 각 선수의 위치를 뽑아낸다.
  - 하키 링크 안에 같은 팀 선수가 총 몇 명인지 계산한다.
하키 링크는 (X, Y)가 가장 왼쪽 아래 모서리인 W * H 크기의 직사각형과, 반지름이 H/2이면서 중심이 (X, Y+R), (X+W, Y+R)에 있는 두 개의 원으로 이루어져 있다. 아래 그림을 참고한다.
선수들의 위치가 주어질 때, 링크 안 또는 경계에 있는 선수가 총 몇 명인지 구하는 프로그램을 작성하시오.

첫째 줄에 수 W H X Y P가 주어진다. P는 선수의 수이다. W와 H는 100보다 작거나 같은 자연수이고, H는 짝수이다. X와 Y는 절댓값이 100보다 작거나 같은 정수이다. P는 최대 50인 자연수이다.
둘째 줄부터 P개의 줄에 각 선수들의 x좌표와 y좌표가 주어진다. 이 좌표는 절댓값이 300보다 작거나 같은 정수이다.

첫째 줄에 링크 안에 있는 선수의 수를 출력한다.
'''

import math

W, H, X, Y, P = map(int, input().split())
radius = int(H/2)
count = 0

for i in range(P):
    x, y = map(int, input().split())
    
    if((x >= X) and (x <= X+W) and (y >= Y) and (y <= Y+H)):
        count += 1
        continue
    elif(math.sqrt(math.pow(X-x, 2)+math.pow((Y+radius)-y, 2)) <= radius):
        count += 1
        continue
    elif(math.sqrt(math.pow((X+W)-x, 2)+math.pow((Y+radius)-y, 2)) <= radius):
        count += 1
        continue
        
print(count)
