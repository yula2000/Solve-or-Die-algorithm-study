from collections import deque
 
for tc in range(1, 11):
    L, start = map(int, input().split())
    data = list(map(int, input().split()))
 
    graph = [[] for _ in range(101)]
 
    for i in range(0, L, 2):
        graph[data[i]].append(data[i + 1])
 
    visited = [0] * 101
 
    q = deque()
    q.append(start)
    visited[start] = 1
 
    while q:
        node = q.popleft()
 
        for next_node in graph[node]:
            if visited[next_node] != 0:
                continue
 
            visited[next_node] = visited[node] + 1
            q.append(next_node)
 
    max_depth = max(visited)
    answer = 0
 
    for i in range(1, 101):
        if visited[i] == max_depth:
            answer = max(answer, i)
 
    print(f'#{tc} {answer}')