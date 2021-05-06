T = int(input())  # 테스트케이스 개수

for i in range(1, T+1):
    a, b = map(int, input().split())
    print("Case #"+str(i)+":", a+b)
