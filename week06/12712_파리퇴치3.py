import sys
sys.stdin = open('12712_input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split()) # 배열크기, M칸스프레이
    arr = [list(map(int, input().split()))for _ in range(N)]
    cnt = 0
    result = []

    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    cx = [-1, -1, 1, 1]
    cy = [-1, 1, -1, 1]

    for x in range(N):
        for y in range(N):
            arr1 = arr[x][y]
            arr2 = arr[x][y]
            
            for k in range(4):
                for m in range(1, M):
                    nx = x + dx[k] * m
                    ny = y + dy[k] * m
                    ux = x + cx[k] * m
                    uy = y + cy[k] * m

                    if 0 <= nx < N and 0 <= ny < N:
                        arr1 += arr[nx][ny]
                    if 0 <= ux < N and 0 <= uy < N:
                        arr2 += arr[ux][uy]
            
            result.append(arr1)
            result.append(arr2)
    answer = max(result)
    print(f'#{tc} {answer}')