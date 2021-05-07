c = int(input())  # 테스트케이스 개수

for i in range(c):
    n = list(map(int, input().split()))  # 학생 수, n명의 점수 입력
    avg = sum(n[1:]) / n[0]  # 평균 전체 점수의 합계 / 학생 수
    cnt = 0  # 평균 이상인 학생 수를 담을 cnt 초기화

    for score in n[1:]:
        if score > avg:
            cnt += 1  # 평균 이상인 학생수 +1
    rate = cnt / n[0]*100  # 평균이 넘는 학생들의 비율 = 평균이상인 학생수 / 전체 학생수 * 100
    print(f"{rate:.3f}%")  # 반올림하여 소수점 셋째짜리까지 출력
