def solution(x):
    digit_sum = sum ([int(n) for n in str(x) ]) #각 자리수의 합
    answer = x % digit_sum == 0
    return answer