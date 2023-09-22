'''
요세푸스 문제는 다음과 같다.
1번부터 N번까지 N명의 사람이 원을 이루면서 앉아있고, 양의 정수 K(≤ N)가 주어진다. 이제 순서대로 K번째 사람을 제거한다. 
한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. 이 과정은 N명의 사람이 모두 제거될 때까지 계속된다. 
원에서 사람들이 제거되는 순서를 (N, K)-요세푸스 순열이라고 한다. 예를 들어 (7, 3)-요세푸스 순열은 <3, 6, 2, 7, 5, 1, 4>이다.
N과 K가 주어지면 (N, K)-요세푸스 순열을 구하는 프로그램을 작성하시오.

첫째 줄에 N과 K가 빈 칸을 사이에 두고 순서대로 주어진다. (1 ≤ K ≤ N ≤ 5,000)

예제와 같이 요세푸스 순열을 출력한다.
'''

N, K=map(int, input().split()) # 사용자로부터 두 개의 정수 입력받기
originalList=[] # 원본 리스트
resultList=[] # 결과 리스트
index=K-1 # 인덱스 번호 저장할 변수 선언 및 초기화

for i in range(N): # i에 0부터 N이 되기 전까지 1씩 증가시킨 값을 대입하며 반복
    originalList.append(i+1);

for i in range(N):
    resultList.append(originalList.pop(index))
    if(len(originalList)==0):
        break
    index = (index + (K-1)) % len(originalList)

print("<", end="")
for i in range(N-1):
    print(resultList[i], ", ", sep="", end="")
print(resultList[N-1], ">", sep="")
