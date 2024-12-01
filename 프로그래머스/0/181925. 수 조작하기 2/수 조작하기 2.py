def solution(numLog):
    
    a = ''
    
    for i in range(len(numLog)):
        if numLog[i] - numLog[i-1] == 1:
            a += 'w'
        if numLog[i] - numLog[i-1] == 10:
            a += 'd'
        if numLog[i] - numLog[i-1] == -1:
            a += 's'
        if numLog[i] - numLog[i-1] == -10:
            a += 'a'
    
    
    answer = a
    return answer