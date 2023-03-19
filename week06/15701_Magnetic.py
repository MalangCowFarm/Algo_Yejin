import sys
sys.stdin = open('15701_input.txt')

T = 10
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr = list(zip(*arr)) # arr 전치행렬 왼쪽이 n극 오른쪽이 s극
    cnt = 0
    
    for i in range(N):
        tmp = [] # 1과 2로만 이루어진 새로운 리스트 만들어줌 (한줄씩검사)
        for j in range(N):
            if arr[i][j] == 1 or arr[i][j] == 2:
                tmp.append(arr[i][j])
        
        for k in range(len(tmp)-1):
            if tmp[k] ==1 and tmp[k+1] == 2:
                cnt +=1        

    print(f'#{tc} {cnt}')