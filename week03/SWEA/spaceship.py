import sys
sys.stdin = open('input.txt')

T = int(input()) # tc
for tc in range(1, T+1):
    N, M = map(int, input().split()) # N 세로 M 가로
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    dx = [-1, 0, 1, -1, 1, -1, 0, 1]
    dy = [-1, -1, -1, 0, 0, 1, 1, 1]

    for i in range(N):
        for j in range(M):
            cnt = 0
            for k in range(8):
                x = j + dx[k]
                y = i + dy[k]

                if 0 <= x < M and 0 <= y < N:
                    if arr[i][j] > arr [y][x]:
                        cnt += 1
            if cnt >= 4:
                result += 1
    print(f'#{tc} {result}')


