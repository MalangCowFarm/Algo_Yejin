"""
"""

def dfs(n):
    global ans
    if n == N: # N 행까지 진행한 경우 -> 성공!
        ans += 1 
        return
    for j in range(N):
        if arr[j] == arr2[n+j] == arr3[n-j] == 0: # 열/ 대각선 모두 Queen 없음
            arr[j] = arr2[n+j] = arr3[n-j] = 1
            dfs(n+1)
            arr[j] = arr2[n+j] = arr3[n-j] = 0

N = int(input()) # N개의 퀸
arr = [0] * N # 각 행이 어느 열에서 선택되었는지 저장될 리스트
arr2 = [0] *(2*N) # 오른쪽 위 대각선 선택되었는지 저장될 리스트
arr3 = [0] *(2*N) # 왼쪽 위 대각선 선택되었는지 저장될 리스트
ans = 0
dfs(0)
print(ans)