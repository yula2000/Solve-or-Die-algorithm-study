'''
간선 정보에 따라 양방향으로 연결
그 후 bfs로 visited를 체크하고, depth도 체크
마지막에 depth 출력

근데 최장거리네?
의문점 1. 최장거리와 최단거리를 확인할 때 뭐가 다른가?
- 어떨때 최장거리가 되고, 어떨때 최단거리가 되는가?
> 이런거 생각할 필요 없이 dfs하기?
>> 수연 : bfs는 모든 노드를 체크할 수 없지만, dfs는 모든 노드를 체크하고 가기에 최장거리가 나온다.

dfs로 탐색

의문점 2. 왜 dfs는 최장거리를 도출하는가?
> 단순히 dfs가 최장거리를 도출하는 것이 아님
    1. 백트레킹으로 그래프 상의 가능한 모든 경로를 탐색함
    2. max를 통해 가장 긴 거리만 저장함
    3. 모든 지점에서 출발함
    >> 그래서 그래프 상 모든 경로 중 가장 긴 거리를 찾게됨

의문점 3. 그럼 N이 10을 넘어가면?
> N = 15만 되도 지구 멸망할 때까지 돌아감
> 다른 방법이 필요
>> 비트마스킹 사용
>> 이건 모르니까 도와줘요 수민히어로!
'''

# 노드번호와 거리를 매개변수로 받음
def dfs(node, dist):
    global answer
    answer = max(answer, dist)

    for next_node in area[node]:
        # 방문하지 않았다면?
        if not visited[next_node]:
            # 방문체크하고
            visited[next_node] = 1
            # dfs 호출
            # > 거리는 +1
            dfs(next_node, dist + 1)
            # 백트레킹을 위해 방문 해제
            visited[next_node] = 0

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    # area만들고
    area = [[] for _ in range(N+1)]
    # 간선 양방향 연결
    for _ in range(M):
        u, v = map(int, input().split())
        area[u].append(v)
        area[v].append(u)

    visited = [0] * (N+1)
    answer = float('-inf')

    # 모든 노드를 돌면서 최장거리 확인
    for i in range(1, N+1):
        # 시작노드 방문 체크
        visited[i] = 1
        # i번 노드에서 거리 1로 탐색 시작
        dfs(i, 1)
        # 시작노드 방문 해제
        # > 다음 노드를 위해
        visited[i] = 0

    print(f'#{tc} {answer}')