def dfs(node, count):
    global answer
    answer = max(answer, count)
    for i in arr[node]:
        if visited[i] != 0:
            continue
        visited[i] = 1
        dfs(i, count+1)
        visited[i] = 0
 
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[] for _ in range(N + 1)]
    for _ in range(M):
        x, y = map(int, input().split())
        arr[x].append(y)
        arr[y].append(x)
    visited = [0] * (N + 1)
    answer = 0
    for start in range(1, N+1):
        visited[start] = 1
        dfs(start, 1)
        visited[start] = 0
    print(f'#{tc} {answer}')