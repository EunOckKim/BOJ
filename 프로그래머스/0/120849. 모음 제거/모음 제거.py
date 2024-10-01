def solution(my_string):
    answer = ''
    
    out_list = ["a","e","i","o","u"]
    
    for i in my_string:
        if i in out_list :
            answer += ''
        else :
            answer += i
    return answer