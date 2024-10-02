import math
                    #math.lcm(6, n) // 6   #LCM 최소공배수

def lcm(a, b):
    return abs(a * b) // math.gcd(a, b)

def solution(n):
    # 6과 n의 최소공배수를 구하고, 이를 6으로 나눔
    return lcm(6, n) // 6

    