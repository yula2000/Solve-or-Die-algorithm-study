from collections import deque

def bfs(start_node):
    visited = [0]*(101)
    q = deque()
    q.append(start_node)
    visited[start_node] = 1
    while q:
        # 해당 레이어에서의 최대값(마지막 턴에서 가장 큰 숫자가 정답이므로)
        answer = max(q)
        # 해당 레이어에서 다음 레이어까지 전화 돌리기
        for _ in range(len(q)):
            node = q.popleft()
            for next_node in adj_list[node]:
                if not visited[next_node]:
                    q.append(next_node)
                    visited[next_node] = 1
    
    return answer


for tc in range(1, 11):
    M, start = map(int, input().split())
    from_to_list = list(map(int, input().split()))

    # 노드가 최대 100개 이므로 101개의 빈 인접리스트 만들기
    adj_list = [[] for _ in range(101)]

    for i in range(M//2):
        node_from = from_to_list[2*i]
        node_to = from_to_list[2*i+1]
        # 인접 리스트 중복 방지
        if node_to not in adj_list[node_from]:
            adj_list[node_from].append(node_to)

    answer = bfs(start)
    print(f'#{tc} {answer}')