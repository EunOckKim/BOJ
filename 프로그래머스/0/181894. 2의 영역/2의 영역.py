def solution(arr):
    answer = []
    lst=[]
    if 2 not in arr:
        return [-1]
    else:
        for i in range(0, len(arr)):
            if arr[i]==2:
                lst.append(i)
    return arr[lst[0]:lst[-1]+1]