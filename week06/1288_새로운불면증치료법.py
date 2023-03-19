import sys
sys.stdin = open('1288_input.txt')

T = int(input())
for t in range(1, T+1):
    N = int(input())
    num_lst = [0] * 10
    cnt = 0
    mul_idx = 0
    while cnt < 10:
        mul_idx += 1
        temp = N * mul_idx
        temp_lst = list(map(int,str(temp)))
        for i in temp_lst:
            if num_lst[i] == 0:
                num_lst[i] = 1
                cnt += 1
 
    print(f'#{t} {temp}')