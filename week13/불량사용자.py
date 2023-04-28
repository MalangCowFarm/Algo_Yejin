from itertools import permutations

def same(user, banned_id):
    for word in range(len(user)):
        if len(user[word]) != len(banned_id[word]): #길이 check
            return False
        for a in range(len(banned_id[word])):
            if banned_id[word][a] == '*' or user[word][a] == banned_id[word][a]: # '*'이거나 문자가 같은 경우
                continue    
            else: # 하나라도 다르면 False
                return False
    return True        

def solution(user_id, banned_id):
    user_per = list(permutations(user_id,len(banned_id)))
    banned_list = []
    
    for user in user_per:
        if same(user, banned_id):
            target = set(user)
            if target not in banned_list:
                banned_list.append(target)  
        else:
            continue
            
    return len(banned_list)