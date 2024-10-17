def solution(a, b):
    answer = 0
    
    pl = int(str(a)+str(b))
    multi = 2*a*b
    
    if pl > multi:
        answer = pl
    else :
        answer = multi
    
    return answer