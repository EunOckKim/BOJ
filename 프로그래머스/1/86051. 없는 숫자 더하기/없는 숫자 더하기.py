def solution(numbers):       #solution이라는 함수 정의. numbers라는 하나의 매개변수를 받음.
    answer = 0               #'answer라는 변수를 0으로 초기화'
    
    for i in range(10):      #0-9까지 반복, 각 값을 i변수에 할당
        if i not in numbers: #만약 i가 numbers 리스트에 없다면
            answer += i      #i의 값을 answer 변수 추가
    
    return answer            # answer의 값을 반환