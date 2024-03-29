'''
과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈다. 주어진 세변의 길이로 삼각형이 직각인지 아닌지 구분하시오.

입력은 여러개의 테스트케이스로 주어지며 마지막줄에는 0 0 0이 입력된다. 각 테스트케이스는 모두 30,000보다 작은 양의 정수로 주어지며, 각 입력은 변의 길이를 의미한다.

각 입력에 대해 직각 삼각형이 맞다면 "right", 아니라면 "wrong"을 출력한다.
'''

while(True): # 무한 반복
    line=list(map(int, input().split())) # 사용자로부터 세 개의 정수를 입력받아 리스트 line에 저장하기
    line=sorted(line) # 리스트 line을 오름차순 정리하여 line에 저장하기
    
    if(line[0]==0 and line[1]==0 and line[2]==0): # 만약, line[0]이 0이고, line[1]도 0이고, line[2]도 0이라면
        break; # 반복문 빠져 나가기
    elif(line[2]*line[2]==line[0]*line[0]+line[1]*line[1]): # 만약, line[0]이 0이 아니거나, line[1]이 0이 아니거나, line[2]이 0이 아니고, line[2]의 제곱이 (line[0]의 제곱 + line[1]의 제곱)과 같다면
        print("right"); # "right" 출력하기
    else: # line[0]이 0이 아니거나, line[1]이 0이 아니거나, line[2]이 0이 아니고, line[2]의 제곱이 (line[0]의 제곱 + line[1]의 제곱)과 같지 않다면
        print("wrong"); # "wrong" 출력하기
