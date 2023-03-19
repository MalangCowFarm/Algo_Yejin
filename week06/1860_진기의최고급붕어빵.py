T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split()) #명수 초 개수
    people = list(map(int, input().split()))
    arr =[0] * (max(people)+1) # 총 초만큼 리스트할당
    
    for i in range(1, len(arr)):
        if i % M == 0:
            arr[i] = K
    cnt = 0
    for p in people:
        for j in range(p,0,-1):
            if arr[j] != 0:
                cnt += 1
                arr[j] -= 1
                break
    
    if cnt == N:
        print(f'#{tc} Possible')
    else:
        print(f'#{tc} Impossible')     