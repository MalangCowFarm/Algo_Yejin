# 셀프넘버
# 양의 정수 n에 대해서 d(n)을 n과 n의 각 자리수를 더하는 함수

num = set(range(1, 10001))
new = set()

for i in range (1, 10001):
    for j in str(i):
        i += int(j)
    new.add(i)
num = num - new # 차집합 하려고 list 말고 set함

for i in sorted(num):
    print(i)