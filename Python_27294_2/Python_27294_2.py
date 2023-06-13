'''
고려대학교 로봇융합관에서 MatKor Cup을 준비하던 주영이는 같이 초밥을 먹자는 동우의 말에 호랭이 초밥 집에 갔다. 
모듬 초밥을 먹으면서 동우와 주영이는 다음과 같은 대화를 하였다.
  동우: "몇개고?"
  주영: "응?"
  동우: "밥알말이다. 몇개고?"
  주영: "그건 또 뭔데?"
  동우: "삼백 이십개다. 훈련된 초밥 장인이 이 한번 스시를 쥘 때 보통은 이 밥알이 삼백 이십개라. 
        점심 식사에는 삼백 이십개가 적당하다 캐도, 오늘 같은 날이나 술하고 같이 낼 때는 이백 팔십개만 해라, 어이? 배 안부르구로"
  주영: "어디서 또 이상한거 배워왔냐"
  동우: "너 혹시 재벌집 막내아들 뭔지 모르나?"
  주영: "모른다"
대한민국을 뒤흔든 드라마를 모른다는 주영이의 말에 동우는 적잖은 충격을 받았다. 
사태의 심각성을 느낀 동우는 주영이가 '재벌집 막내아들'을 보게 하기 위해 MatKor 사람들을 모았다. 
주영이에게 그냥 영상을 보여주는 것보다 알고리즘을 이용해서 알려주어야 흥미를 가지게 할 수 있다고 생각한 MatKor 사람들은 
주영이가 드라마에 흥미를 가지게 하기 초밥 밥알 갯수로 문제를 만들기로 했다. 
자 MatKor에서 문제를 만들었고, 동우가 주영이에게 문제를 말했다.
  동우: "오늘 나는 너가 만든 초밥을 먹을 거야. 너는 '재벌집 막내아들'의 진양철 회장님의 말에 따라 술하고 같이 초밥을 먹거나 점심 식사가 아닐 때는 
        초밥의 밥알을 280개로 하며, 점심 식사이면서 술과 같이 먹지 않을때는 초밥의 밥알을 320개로 하여 초밥을 만들어야 해, 
        근데, 내가 초밥을 언제 먹을지, 혹은 술과 같이 먹을지 아직 정하지 않았어. 내가 초밥을 먹는 시간과 술의 유무를 말하면, 
        그때 너는 너가 만들어야 하는 초밥의 밥알 갯수를 구해야해"
당신은 위의 문제를 읽고 주영이를 대신하여 동우의 문제를 해결하여라.

첫 번째 줄에 시간을 의미하는 정수 T (0 <= T <= 23)와 술의 유무를 의미하는 정수 S (0 <= S <= 1)가 공백으로 구분되어 주어진다. 
T가 11이하이면 아침 시간, 12이상 16 이하이면 점심 시간, 그렇지 않으면 저녁 시간을 뜻한다. S가 1 이면 술과 함께 먹는 것을 의미하며, 
0 이면 술 없이 초밥을 먹는 것을 의미한다.

첫 번째 줄에 주영이가 만들어야 하는 초밥 하나의 밥알의 갯수를 출력하여라.
'''

T, S=map(int, input().split()) # 사용자로부터 두 개의 정수 입력받기

if(S==0 and T>=12 and T<=16): # 만약, S가 0이고, T가 12보다 크거나 같고, T가 16보다 작거나 같다면
    print("320") # "320" 출력하기
else: # S가 0이 아니거나, T가 12보다 작거나, T가 16보다 크다면
    print("280") # "280" 출력하기
