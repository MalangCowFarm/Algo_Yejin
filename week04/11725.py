def bfs():
    now = 1
    stack=[now]
    
    #자식을 인덱스하는데 자식은 많이있고 부모는 한명이니까
    while stack:
        now = stack.pop(0)
        # visited[now] = 
        for i in edge[now]:
            if not visited[i]:
                visited[i] = now
                stack.append(i)
    
    print(*visited[2:])

N = int(input())
edge = [[] for i in range(N+1)]

visited = [0] * (N+1) 
for i in range(N-1):
    a, b = map(int, input().split())
    edge[a].append(b) # 노드 n에 접근하는 애가 여러명일 수있으니까 apppend
    edge[b].append(a) 
    # 방향성이 없으면 무조건 양방향 해야함

bfs()