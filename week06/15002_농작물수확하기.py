import sys
sys.stdin = open('15002_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 농장크기
    arr = [list(map(int, input())) for _ in range(N)]
    M = N//2
    ans = 0

    for i in range(N):
        for j in range(abs(N//2-i), N-abs(N//2-i)): # 범위 주의!
            ans += arr[i][j]
    print(f'#{tc} {ans}')