import sys
# sys.stdin = open('input2.txt')
input = sys.stdin.readline

"""

"""


INF = int(1e9)
n = int(input())

colors = [[0, 0, 0]] # range 맞추려고 colors[0] 값 맞춰줌
for _ in range(n):
    colors.append(list(map(int, input().split())))

ans = INF

for i in range(3):  # R, G, B 각각 시작할때
    dp = [[0]*3 for _ in range(n+1)] 
    dp[1] = [INF, INF, INF]
    dp[1][i] = colors[1][i] # dp[1][G]와 dp[1][B] 값을 각각 INF로 설정하면 무조건 R에서 시작함을 보장

    for j in range(2, n+1): # 1일때는 위에서 했으니까 2부터 시작
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + colors[j][0]
        dp[j][1] = min(dp[j-1][2], dp[j-1][0]) + colors[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + colors[j][2]
    
    dp[n][i] = INF
    ans = min(ans, min(dp[n]))

print(ans)