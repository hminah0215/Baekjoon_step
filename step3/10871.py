n, x = map(int, input().split())
a = list(map(int, input().split()))  # 정수 n개로 이루어진 수열

for i in range(n):
    if a[i] < x:
        print(a[i], end=" ")  # 공백으로 구분해서 출력하기
