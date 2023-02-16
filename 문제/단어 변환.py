#단어 변환
from collections import deque

def canChange(begin, word):
    count = 0
    for i in range(len(word)):
        if begin[i] == word[i]:
            count += 1
    if count == len(begin)-1:       #조건: 한 번에 한 개의 알파벳만 바꿀 수 있습니다.
        return True
    return False

def bfs(begin, target, words):
    visited = [False] * len(words)
    if target not in words:
        return 0
    count = 0
    queue = deque()
    queue.append((begin, count))
    while queue:
        begin, count = queue.popleft()
        if begin == target: return count
        for i in range(len(words)):
            if canChange(begin, words[i]) and visited[i] == False:
                queue.append((words[i], count+1))
                visited[i] = True
    return 0

def solution(begin, target, words):
    return bfs(begin, target, words)