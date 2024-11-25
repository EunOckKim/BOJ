def solution(num_list):
    answer = 0
        
    add = 0
    mani = 1
    
    for i in num_list:
        add += i
        mani *= i
        
    if add*add > mani :
        answer = 1
    else :
        answer = 0
        

    return answer