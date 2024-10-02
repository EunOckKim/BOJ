def solution(n):
    answer = 0
    
    if n % (n**(1/2)) == 0 :          # n ** (1/2)가 제곱근
        answer = 1
    else :
        answer = 2
    return answer