'''
N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

첫째 줄에 숫자의 개수 N (1 ≤ N ≤ 100)이 주어진다. 둘째 줄에 숫자 N개가 공백없이 주어진다.

입력으로 주어진 숫자 N개의 합을 출력한다.
'''

N=int(input()) # 사용자로부터 정수 입력받기
s=input() # 숫자들을 문자열로 입력받기
sum=0 # 변수 sum 선언 및 초기화

for i in s: # 문자열 s에 담긴 내용 하나씩 i에 넣어가며 반복 
    sum+=int(i) # sum에 sum+int(i)의 값 대입하기

print(sum) # 결론 출력하기
