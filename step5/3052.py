numbers = []

for i in range(10):
    n = int(input())  # 10개의 정수 입력
    numbers.append(n % 42)  # 42로 나눈 나머지

# 중복을 허용하지 않는 set으로 자료형 변환
num = set(numbers)
print(len(num))  # 서로 다른 나머지가 몇개 있는지 출력
