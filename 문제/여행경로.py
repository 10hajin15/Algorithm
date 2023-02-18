#여행경로
def dfs(curAirport, tickets, result):
    result.append(curAirport)
    canAirport = []
    for i in tickets:
        if i[0] == curAirport:
            canAirport.append(i[1])
    canAirport.sort()
    if len(canAirport) == 0 and len(tickets) == 0:
        return result
    for j in canAirport:
        if len(tickets) == 0:
            break
        index = tickets.index([curAirport, j])
        tickets.remove([curAirport, j])
        dfs(j, tickets, result)
        if len(tickets) == 0: return result
        result.pop()
        tickets.insert(index, [curAirport, j])
def solution(tickets):
    result = []
    return dfs("ICN", tickets, result)

#print(solution([["ICN", "A"], ["A", "B"], ["A", "C"], ["C", "A"], ["B", "D"]]))




