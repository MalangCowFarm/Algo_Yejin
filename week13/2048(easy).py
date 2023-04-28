import sys 
sys.stdin = open('input1.txt')
# input = sys.stdin.readline

"""
어려어 ;; 
"""

from collections import deque
from copy import deepcopy

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def move(arr, di):
   
    plus_cand = [[True] * n for _ in range(n)]

    # 위 또는 왼쪽으로 이동
    if di in [0, 3]:
        start, end, go = 0, n, 1

    # 아래 또는 오른쪽으로 이동
    else:
        start, end, go = n-1, -1, -1

    # 움직임이 필요한 값들은 움직
    for i in range(start, end, go):
        for j in range(start, end, go):
            if arr[i][j] == 0:
                continue
            x, y = i, j
            value = arr[x][y]
            arr[x][y] = 0
            nx, ny = x + dx[di], y + dy[di]

            while True:
                if nx < 0 or nx >= n or ny < 0 or ny >= n:
                    break

                # 다음 이동 좌표비면 이동
                if arr[nx][ny] == 0:
                    x, y = nx, ny
                    nx, ny = x + dx[di], y + dy[di]

                elif arr[nx][ny] == value and plus_cand[nx][ny]:
                    x, y = nx, ny
                    plus_cand[x][y] = False
                    break

                else:
                    break
            arr[x][y] = arr[x][y] + value

    return arr

def bfs(arr):

    q = deque([arr])
    max_value = -1
    go = 0

    while q:
        size = len(q)

        for _ in range(size):
            arr = q.popleft()

            for di in range(4):
               
                next_arr = move(deepcopy(arr), di)
                q.append(next_arr)

                for i in range(n):
                    for j in range(n):
                        if next_arr[i][j] > max_value:
                            max_value = next_arr[i][j]      

        go += 1

        if go == 5:
            return max_value

##################################################################

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

print(bfs(arr))