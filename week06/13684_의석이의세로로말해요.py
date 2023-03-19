import sys
sys.stdin = open('13684_input.txt')

# T = int(input()) 
# for tc in range(1, T+1):
#     arr = [list(input()) for _ in range(5)]
#     ans = ''
#     leg = []
#     for i in arr:
#         leg.append(len(i))
#     length = max(leg)

#     for i in range(length):
#         for j in range(5):
#             try:
#                 ans += arr[j][i]
#             except:
#                 pass
    
#     print(f'#{tc} {ans}')

T = int(input())
  
for tc in range(1, T+1):
    word_list = [input() for _ in range(5)]
    str_s = ''
    for i in range(15): # 길이가 15 이하인 문자열 주어져서 범위 15이하로 함
        for j in range(5):
            str_s += word_list[j][0+i:1+i] # 문자열은 슬라이싱 해도 index error 안남

    print(f'#{tc} {str_s}')