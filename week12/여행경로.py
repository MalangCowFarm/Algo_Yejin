def solution(tickets):
    dic = {}

    for ticket in tickets:
        dic[ticket[0]] = dic.get(ticket[0], []) + [ticket[1]]

    for key in dic.keys(): 
        dic[key].sort(reverse=True)
            
    stack = ["ICN"]
    path = []

    while stack:
        top = stack[-1]
        if top not in dic or len(dic[top]) == 0: 
            path.append(stack.pop())
        else:
            stack.append(dic[top][-1])
            dic[top].pop() 
            
    return path[::-1]