#카펫
def solution(brown, yellow):
    total = brown + yellow
    for i in range(1, total+1):
        rest = total % i
        if rest == 0:
            share = total // i
            if i >= share and (i-2) * (share-2) == yellow:
                return [i,share]


print(solution(8, 1))