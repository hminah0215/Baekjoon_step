# 세자리 수 곱하기 세자리 수 일때 단계별 계산값
a = int(input())   # 기본값
b = list(input())  # 곱할값을 list로 저장

c1 = a * int(b[2])  # a * 곱셈할 값의 일의자리 수
c2 = a * int(b[1])
c3 = a * int(b[0])

answer = (c1 + (c2*10) + (c3*100))
print(c1, c2, c3, answer)
