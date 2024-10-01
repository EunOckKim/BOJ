import math

def solution(numer1, denom1, numer2, denom2):
    answer = []
    
    
    a = (numer1 * denom2)+(numer2 * denom1)
    b = denom1 * denom2
    
    gcd = math.gcd(a, b)
    
    answer.append(a//gcd)
    answer.append(b//gcd)
    return answer