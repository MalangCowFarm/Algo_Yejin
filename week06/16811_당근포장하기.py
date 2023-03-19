import sys
sys.stdin = open('16811_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input()) # 당근 개수
    arr = list(map(int, input().split()))
    arr.sort() # 오름차순 정렬

    minV = 1000
    for i in range(N-2): # 소 박스
        for j in range(i+1, N-1): # 중박스
            if arr[i] != arr[i+1] and arr[j] != arr[j+1]: # 경계지점 애들 달라야함
                A = i + 1
                B = j -i
                C = N -1 -j
                if A * B * C != 0 and A <= N//2 and B <= N//2 and C <= N//2: # 빈 박스 없고 절반 초과하는 박스도 없으면
                    if minV > max(A, B, C) - min(A, B, C):
                        minV = max(A, B, C) - min(A, B, C)

    if minV == 1000:
        minV = -1

    print(f'#{tc} {minV}')
# ==========================================================
for tc in range(1, T + 1):
    N = int(input())
    carrot = list(map(int, input().split()))
    carrot.sort()
    ans = 1000

    for i in range(N - 2):
        for j in range(i + 1, N - 1):
            small = carrot[:i + 1]
            middle = carrot[i + 1:j + 1]
            big = carrot[j + 1:]
            if small[-1] < middle[0] and middle[-1] < big[0]:
                A = len(small)
                B = len(middle)
                C = len(big)
                MAX = max(A, B, C)
                MIN = min(A, B, C)
                if MAX > N // 2 or MIN == 0:
                    pass
                else:
                    ans = min(ans, MAX - MIN)
    if ans == 1000:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {ans}')
