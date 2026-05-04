def dfs(now_node, cur_distance):
    global max_distance

    if cur_distance > max_distance:
        max_distance = cur_distance

    visited[now_node] = 1

    for next_node in graph[now_node]:        
        if not visited[next_node]:
            dfs(next_node, cur_distance+1)  # dfs(graph[next_node], count+1) 가 아니라 next_node 번호만 던져줘야됨(리스트면 에러남)
    
    visited[now_node] = 0  # visited[next_node] = 0 이라써서 또 틀림 > for문 안에 있어야 next_node변수가 유효함/밖으로 나가면 정의한적 없음

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    # visited = [0]*(N+1)

    # max_distance = 1
    # dfs(1, 1)
    # print(f"#{tc} {max_distance}")

    answer = 0
    for i in range(1, N+1):
        max_distance = 0
        visited = [0]*(N+1)
        dfs(i, 1)
        answer = max(answer, max_distance)

    print(f"#{tc} {answer}")
