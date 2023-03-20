#2016년
weekend = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED']
day = [0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def solution(a, b):
    total = 0
    for i in range(1, a):
        total += day[i]
    result = (total + b) % 7
    return weekend[result]

print(solution(5, 24))