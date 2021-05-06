natural_num = []  # 9개의 자연수를 담을 리스트

for i in range(9):
    natural_num.append(int(input()))  # append() 함수로 리스트에 입력값 추가

max_num = max(natural_num)  # 자연수 리스트에서 최댓값구하기

print(max_num)  # 최댓값 출력

# 최대값이 리스트에서 몇번째 수 인지 구하기 index 는 0부터 시작이니 +1
print(natural_num.index(max_num)+1)
