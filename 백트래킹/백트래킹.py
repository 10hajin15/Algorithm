'''
#백트래킹
- 임의의 집합에서 주어진 기준대로 원소의 순서(순열)를 선택하는 문제를 푸는 데 적합
- 트리 자료구조의 변형된 깊이우선탐색(DFS)
- 모든 문제 사례에 대해서 효율적이지 않음
  ex) n-Queens, 부분 지합의 합, 0-1 배낭문제, etc

- 상태공간트리(State Space Tree)
  상태 공간 : 해답을 탐색하기 위한 탐색 공간
  상태공간트리: 탐색 공간을 트리 형태의 구조로 '암묵적으로' 해석

- 백트래킹 기법
  상태공간트리를 깊이우선탐색(DFS)으로 탐색
  방문 중인 노드에서 더 하위 노드로 가면 해답이 없을 경우
   -> 해당 노드의 하위 트리를 방문하지 않고 부모 노드로 되돌아 감(backtrack)

- 유망함(promising)
  방문 중인 노드에서 하위 노드가 해답을 발견할 가능성이 있으 유망(promising)
  하위 노드에서 해답을 발견할 가능성이 없으면 유망하지 않음(nonpromising)

- 백트래킹과 가지치기(pruning)
  백트래킹: 상태공간트리를 DFS로 탐색
  방문 중인 노드가 유망한지 체크
  만약 유망하지 않으면, 부모 노드로 되돌아감(backtrack)

- 가지치기(pruning)
  유망하지 않으면 하위 트리를 가지치기함
  가지치기한 상태: 방문한 노드의 방문하지 않는 하위 트리(pruned state)

void checknode(node v)
{
    node u;
    if (promising(v))
      if (v에 해답이 있으면)
        해답을 출력;
      else
        for (v의 모든 자식 노드 u에 대해서)
          checknode(u);
}

- 백트래킹 알고리즘의 구현
  상태공간트리를 실제로 구현할 필요는 없음
  현재 조사중인 가지의 값에 대해 추적만 하면 됨
  상태공간트리는 암묵적으로 존재한다고 이해하면 됨

- n-Queens 문제
  8-Queens(n=8)문제의 일반화된 문제
  n x n 체스보드에 n개의 퀸을 배치하는 문제
    -> 어떤 퀸도 다른 퀸에 의해서 잡아먹히지 않도록 배치해야 함
    -> 즉, 같은 행, 열, 대각선에는 다른 퀸을 놓을 수 없음
- n-Queens 문제: 백트래킹
  백트래킹으로 문제 해결:
    -> 임의의 집합에서 기준에 따라 원소의 순서를 선택
  n-Queens 문제에 적용:
    -> 임의의 집합(set): 체스보드에 있는 n2(제곱)개의 가능한 위치
    -> 기준(criterion): 새로 놓을 퀸이 다른 퀸을 위협할 수 없음
    -> 원소의 순서(sequence): 퀸을 놓을 수 있는 n개의 위
- n-Queens 문제의 해결
  기본 가정: 같은 행(row)에는 퀸을 놓지 않는다.
  유망 함수의 구현: 같은 열(column)이나 같은 대각선(diagonal)에 놓이는 지를 확인
  - 유망의 조건 1: 같은 열 체크
    col[i]: i번째 행(row)에서 퀸이 놓여있는 열(column)의 위치
    col[k]: k번째 행(row)에서 퀸이 놓여있는 열(column)의 위치
    col[i] == col[k]: 같은 열에 놓이게 되므로, 유망하지 않다.
  - 유망의 조건 2: 대각선 체크
    왼쪽에서 위협하는 퀸에 대해서
      열에서의 차이는 행에서의 차이와 같다
      col[i] - col[k] == i - k
    오른쪽에서 위협하는 퀸에 대해서
      열에서의 차이는 행에서의 차이의 마이너스 같다
      col[i] - col[k] == k - i
    => col[i]와 col[k]의 절댓값으로 대각선 위협 판단

출처: https://youtu.be/HRwFgtiqHH0
'''

def promising(i, col):
    k = 1
    flag = True
    while (k < i and flag):
        if(col[i] == col[k]) or (abs(col[i] - col[k]) == (i - k)):
            flag = False
        k += 1
    return flag

def n_queens(i, col):
    n = len(col) - 1
    if (promising(i, col)):
        if (i == n):
            print(col[1 : n + 1])
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                n_queens(i + 1, col)

n = 4
col = [0] * (n + 1)
n_queens(0, col)
