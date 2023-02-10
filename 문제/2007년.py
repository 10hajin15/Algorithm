#2007년
x, y = map(int, input().split())

weekend = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

total = 0
for i in range(1, x):
    total += day[i]
result = (total + y) % 7
print(weekend[result])


