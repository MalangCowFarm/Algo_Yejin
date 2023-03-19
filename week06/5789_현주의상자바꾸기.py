import sys
sys.stdin = open('5789_input.txt')

T = int(input())
for tc in range(1, T+1):
    N, Q = map(int, input().split())
    arr = [0 for i in range(1, N+1)]
    for i in range(1, Q+1):
        L, R = map(int, input().split())
        for j in range(L-1, R):
            arr[j] = i

    print(f'#{tc}', *arr)

    