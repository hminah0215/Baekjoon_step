# 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다.
a = int(input())  # 150
b = int(input())  # 266
c = int(input())  # 427

# 곱한 결과를 문자열로 변환 후 리스트에 담는다
m = str(a * b * c)  # "17037300"
result = list(m)

for i in range(10):  # 1부터 9까지의 숫자가 몇번 쓰였는지 한줄에 하나씩 출력
    print(result.count(str(i)))
    '''
    결과, 0이 3번, 1일 1번, 3이 2번, 7이 2번쓰였음
    3
    1
    0
    2
    0
    0
    0
    2
    0
    0
    '''
