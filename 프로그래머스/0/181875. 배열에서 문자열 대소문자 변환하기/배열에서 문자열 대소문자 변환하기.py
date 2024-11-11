def solution(strArr):
    # 결과를 저장할 리스트
    result = []
    
    # 배열을 순회하면서 짝수/홀수 인덱스 처리
    for i, s in enumerate(strArr):
        if i % 2 == 0:  # 짝수번째 인덱스
            result.append(s.lower())
        else:  # 홀수번째 인덱스
            result.append(s.upper())
    
    return result
