def solution(myString):
    answer = []
    
    myStrin = myString.split("x")
    
    for i in myStrin:
        answer.append(len(i))
        
    return answer