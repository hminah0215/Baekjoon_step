# 구구단 출력, step3 는 for문이니까 그거 사용함
n = int(input())

for i in range(1, 10):
    print("{} * {} = {}".format(n, i, n*i))
