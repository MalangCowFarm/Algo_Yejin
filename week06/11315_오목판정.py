import sys
sys.stdin = open('11315_input.txt')

dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]

def omok():
    for x in range(N):
        for y in range(N):
            if arr[x][y] == 'o':
                for k in range(4):
                    cnt = 1
                    for multi in range(1, 5):
                        nx = x + dx[k]*multi
                        ny = y + dy[k]*multi

                        if 0<= nx < N and 0<= ny < N:
                            if arr[nx][ny] == 'o':
                                cnt += 1

                                if cnt == 5:
                                    return 'YES'
                            elif arr[nx][ny] == '.':
                                break
    return 'NO'

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 문자열 길이
    arr = [list(input()) for _ in range(N)]

    print(f'#{tc} {omok()}')

                    
                