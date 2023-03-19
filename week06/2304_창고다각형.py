import sys
sys.stdin = open('2304_input.txt')

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)] #위치, 높이
height = 0
state = 0
for i in range(N):
    if arr[i][0] >= height:
        height = arr[i][0]
        state = arr[i][1]

cnt = 0

now = 0
now_height = 0
for i in range(N):
    if arr[i][0] == state:
        cnt += abs(arr[i-1][0] - now) * now_height
        break
    else:
        if arr[i][1] > now_height:
            cnt += (arr[i][0] - now) * now_height
            now_height = arr[i][1]
            now = arr[i][0]

now = 0
now_height = 0
for i in range(N-1, -1, -1):
    if arr[i][0] == state:
        cnt += abs(arr[i][0] - now) * now_height
        break
    else:
        if arr[i][1] > now_height:
            cnt += (arr[i][0] - now) * now_height
            now_height = arr[i][1]
            now = arr[i][0]
print(cnt)




