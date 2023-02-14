#파도반 수열
for t in range(int(input())):
    n = int(input())
    d = [0, 1, 1, 1, 2]
    for i in range(5, n+1):
        d.append(d[i-1] + d[i-5])
    print(d[n])