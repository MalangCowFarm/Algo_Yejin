import sys
sys.stdin = open('9490_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int ,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt = 0
    cnt_lst = []
    for x in range(N):
        for y in range(M):
           cnt = arr[x][y]
           multi = cnt
           for k in range(4):
               for mul in range(1, multi+1):
                   nx = x + dx[k]*mul
                   ny = y + dy[k]*mul
                   if 0 <= nx < N and 0 <= ny < M:
                       cnt += arr[nx][ny]

           cnt_lst.append(cnt)

    print(f'#{tc}', max(cnt_lst))

