'''
bfs에서 queue의 길이 만큼만 반복하는 방법 이용
> 레벨 별 탐색
그래서 매 depth의 노드 번호들 중 가장 큰 노드번호를 저장
while이 끝나면 전 depth의 가장 큰 노드번호 반환
'''
from collections import deque

def bfs(start):
    # 시작지점 queue에 넣고
    queue = deque([start])
    # 방문체크
    visited[start] = 1

    # 매 depth의 가장 큰 노드 번호를 저장하기 위한 변수
    result = 0

    while queue:
        # 매 depth의 가장 큰 노드 번호 저장
        result = max(queue)

        # queue의 길이만큼만 반복
        for _ in range(len(queue)):
            curr_node = queue.popleft()

            for next_node in graph[curr_node]:
                # 방문하지 않은 노드라면
                if not visited[next_node]:
                    # 방문 체크하고
                    visited[next_node] = 1
                    # queue에 넣기
                    queue.append(next_node)

    # while문이 끝나면 마지막 depth의 가장 큰 노드번호를 반환
    return result

for tc in range(1, 11):
    N, start_node = map(int, input().split())
    edges = list(map(int, input().split()))

    graph = [[] for _ in range(101)]
    for i in range(0, N, 2):
        u, v = edges[i], edges[i+1]
        # 단방향 연결
        graph[u].append(v)

    visited = [0] * 101

    answer = bfs(start_node)
    print(f'#{tc} {answer}')