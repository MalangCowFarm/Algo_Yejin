import sys
# sys.stdin = open('input.txt')
input = sys.stdin.readline
sys.setrecursionlimit(10000)

"""

"""
n = int(input()) # 수열길이
arr = list(map(int, input().split())) # 10 20 10 30 20 50
dp = [1] * (n+1)

for i in range(len(arr)): # 배열 길이만큼돈다.
    for j in range(i): # 해당 배열 원소의 직전 원소까지 돈다.
        if arr[j] < arr[i]:  # 만약 해당 원소가 전 원소보다 크다면
            dp[i] = max(dp[i], dp[j]+1)
            # 전 원소에 저장되어 있는 최장수열길이에서 +1 값과 저장되어있는 수열길이값을 비교해서 큰값을 대입

num = max(dp)
print(num) 

ans = []
for i in range(n-1, -1, -1):
    if dp[i] == num: 
        ans.append(arr[i]) 
        num -= 1 

ans.reverse()
for i in ans:
    print(i, end=' ')