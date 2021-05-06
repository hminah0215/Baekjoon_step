n = int(input())  # 정수의 개수
numbers = list(map(int, input().split()))  # 정수의 개수만큼 정수 입력

# 가장 크거나 작은수를 리스트의 0번째것으로 본다고 가정
max_num = numbers[0]
min_num = numbers[0]

for n in numbers:

    if n > max_num:
        max_num = n
    elif n < min_num:
        min_num = n

print(min_num, max_num)
