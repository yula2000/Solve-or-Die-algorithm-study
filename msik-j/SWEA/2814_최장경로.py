def dfs(now_node, visits):
    global answer
    if answer < visits:
        answer = visits

    # 다음 노드에 대해서 DFS 수행 세팅
    for next_node in adj_list[now_node]:
        # 방문한 적 없으면 방문처리 후 DFS 수행(visits+1)
        if not visited[next_node]:
            visited[next_node] = 1
            dfs(next_node, visits+1)
            # visits 원복
            visited[next_node] = 0


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    adj_list = [[] for _ in range(N+1)]

    # 인접 리스트 받기
    for _ in range(M):
        a, b = map(int, input().split())
        adj_list[a].append(b)
        adj_list[b].append(a)

    # 아무 연결이 없으면 최장 경로는 1
    answer = 1
    visited = [0]*(N+1)
    
    # 모든 노드를 시작으로 반복문
    for node in range(1, N+1):
        visited[node] = 1
        dfs(node, 1)
        visited[node] = 0

    print(f"#{tc} {answer}")