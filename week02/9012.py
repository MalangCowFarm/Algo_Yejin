N = int(input()) # tc

for i in range(N):
    stack = []
    word = input()
    for j in word:
        if j == '(':
            stack.append(j)
        elif j == ')':
            if stack:
                stack.pop()
            else: # 스택에 괄호 없을 때
                print("NO")
                break
    else:
        if len(stack) == 0: 
            print("YES")
        else:
            print("NO")

# 근데 이 방법 보다 문자열로 푸는게 나을듯