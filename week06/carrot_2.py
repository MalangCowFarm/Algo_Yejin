import sys
sys.stdin = open('16811_input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = list(map(int, input().split()))
    arr.sort()

    min_V = 1000

    for i in range(N-2):
        for j in range(i+1, N-1):
            small = arr[:i+1]
            medium = arr[i+1: j+1]
            big = arr[j+1:]

            if small[-1] < medium[0] and medium[-1] < big[0]:
                A = len(small)
                B = len(medium)
                C = len(big)

                MAX = max(A, B, C)
                MIN = min(A, B, C)

                if MAX > N//2 or MIN <= 0:
                    pass
                else:
                    ans = MAX - MIN

                    min_V = min(ans, min_V)

    if min_V == 1000:
        min_V = -1

    print(f'#{tc} {min_V}')
