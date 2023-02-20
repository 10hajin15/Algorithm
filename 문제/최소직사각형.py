#최소직사각형
def solution(sizes):
    maxW = 0
    maxH = 0
    for w, h in sizes:
        if w < h:
            w, h = h, w
        maxW = max(maxW, w)
        maxH = max(maxH, h)
    return maxW * maxH

print(solution([[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]))

# def solution(sizes):
#     return max(max(x) for x in sizes) * max(min(x) for x in sizes)