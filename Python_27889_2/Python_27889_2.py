"""
GEC에는 여러 학교가 있다. 각 학교의 약칭과 정식 명칭은 다음과 같다.
  -NLCS: North London Collegiate School
  -BHA: Branksome Hall Asia
  -KIS: Korea International School
  -SJA: St. Johnsbury Academy
학교 이름을 좋아하는 규빈이는, 학교 이름을 짧게 부르는 것을 싫어하기 때문에, 각 학교의 약칭이 주어졌을 때 정식 명칭을 출력하는 프로그램을 만들기로 하였다.
각 학교의 약칭이 주어졌을 때, 정식 명칭을 출력하는 프로그램을 작성하시오.

첫 번째 줄에 학교의 약칭 중 하나가 주어진다.

첫 번째 줄에 입력된 학교의 정식 명칭을 출력한다.
"""

S=input() # 사용자로부터 문자열 입력받기
shortName=['NLCS', 'BHA', 'KIS', 'SJA']
longName=['North London Collegiate School', 'Branksome Hall Asia', 'Korea International School', 'St. Johnsbury Academy']

for i in shortName:
    if i==S:
        print(longName[shortName.index(S)])
        break
