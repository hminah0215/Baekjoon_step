n = int(input())  # ox퀴즈 문제 개수

for i in range(n):
    ox_list = list(input())  # ooxxoxxooo 와 같은 ox퀴즈 결과를 담는 리스트
    scores = 0  # 점수
    sum_sc = 0  # 점수의 합 초기화

    for j in ox_list:
        if j == "O":  # ox퀴즈 결과 리스트에서 'o'가 연속으로 나오면 +1점
            scores += 1
            sum_sc += scores
        else:
            scores = 0
    print(sum_sc)  # 총 점수 출력
