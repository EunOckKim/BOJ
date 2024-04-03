def solution(arr1, arr2):
    answer =  []    #결과값 행렬 저장할 빈 리스트 생성
    
    for i in range (len(arr1)):  #arr1의 행 개수만큼 반복
        arr_sum = []           #현재 행에 대한 빈 리스트 생성
        for j in range(len(arr1[0])):      #arr1의 열 개수만큼 반복
            arr_sum.append(arr1[i][j] + arr2[i][j])# 같은 위치에 있는 두 행렬을 더하여 row에 추가
        answer.append(arr_sum) #현재행 row를 행렬에 추가 
    return answer