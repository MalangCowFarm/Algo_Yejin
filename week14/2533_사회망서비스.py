def dfs(v):

    visited[v]=True 

    for next in arr[v]: 
        if(visited[next]): 
            continue 
        
        dfs(next) 
        dp[v][0]+=dp[next][1] 
        dp[v][1]+=min(dp[next]) 

########################################

N = int(input())
arr = [[] for _ in range(N+1)]
visited=[False]*(N+1)

dp= [[0,1] for _ in range(N+1)]

for i in range(N-1):
    f,t=map(int,input().split())
    arr[f].append(t)
    arr[t].append(f)

dfs(1) 
print(min(dp[1]))