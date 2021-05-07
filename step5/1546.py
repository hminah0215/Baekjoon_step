n = int(input())  # 시험 본 과목 개수
scores = list(map(int, input().split()))  # 시험 점수
max_score = max(scores)  # 가장 잘본 과목의 점수

for i in range(n):
    scores[i] = scores[i]/max_score * 100  # 고칠 점수 계산식
    avg = sum(scores)/n  # 고친점수의 평균
print(round(avg, 2))  # 소수점 둘째자리까지 출력
