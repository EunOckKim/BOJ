def solution(arr, queries):
    answer = []
    
    for a,b,c in queries:
        mid =[]
        for i in arr[a: b+1] :
            if i > c:
                mid.append(i)
        answer.append(-1 if not mid else min(mid))
    return answer