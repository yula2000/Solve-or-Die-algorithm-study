from collections import deque

T = int(input())

# 대각선까지 delta는 8방향
delta = [(1,0), (0,1), (-1,0), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]

for tc in range(1, T+1):
    N = int(input())
    # 지뢰찾기 지도
    graph = [list(input()) for _ in range(N)]
    # 방문 처리
    visited = [[0]*N for _ in range(N)]
    # 0인 애들 좌표 모으기
    start_nodes = []
    # 지뢰 개수
    bombs_cnt = 0

    # 지뢰찾기 지도를 이제 숫자로 변환하기(지뢰 제외)
    for r in range(N):
        for c in range(N):
            # 주변 지뢰 개수를 받을 변수
            cnt = 0
            # 여기서 지뢰 개수 세주기
            if graph[r][c] == '*':
                bombs_cnt += 1
                continue
            # 8방향 탐색 후 해당 '.'을 숫자 값으로 변환
            for dir in range(8):
                nr, nc = r + delta[dir][0], c + delta[dir][1]
                if 0 <= nr and nr < N and 0 <= nc and nc < N:
                    if graph[nr][nc] == '*':
                        cnt += 1
            graph[r][c] = cnt

            # 8방향 탐색하고 0인 경우 start_nodes에 추가
            if cnt == 0:
                start_nodes.append((r,c))
    
    # 0인 칸의 개수
    zeros_cnt = len(start_nodes)
    
    # 0도 아니고 지뢰도 아닌 애들에 대하여 bfs를 수행하면서 개수를 세줄 것
    # 0을 클릭할 때 오픈 되는 애들이라고 생각하면 됨
    not_zero_cnt = 0

    # bfs니까 deque 활용
    q = deque()
    # answer => 클릭 횟수
    answer = 0

    # 0인 좌표 애들에 대해서 bfs를 수행 
    for start_r, start_c in start_nodes:
        # 당연히 방문 처리된 경우는 할 필요 없음(클릭도!)
        if visited[start_r][start_c]:
            continue

        # 방문처리 후 q에 append
        visited[start_r][start_c] = 1
        q.append((start_r, start_c))

        # 이 과정 자체를 클릭으로 볼 것이므로 answer += 1
        answer += 1
        # bfs 수행
        while q:
            cr, cc = q.popleft()
            for dir in range(8):
                nr, nc = cr + delta[dir][0], cc + delta[dir][1]
                if 0 <= nr and nr < N and 0 <= nc and nc < N and not visited[nr][nc]:
                    # 지뢰면 continue
                    if graph[nr][nc] == '*':
                        continue
                    # 0이면 다음 bfs 수행을 위해 방문처리 후 q에 append
                    elif graph[nr][nc] == 0:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                    # 이제 0도 아니고 지뢰도 아닌 애들 -> 0을 클릭 했는데 오픈되는 숫자들
                    # 방문처리도 하고 not_zero_cnt 개수를 세준다
                    else:
                        visited[nr][nc] = 1
                        not_zero_cnt += 1
    
    # 그럼 이제 0을 다 눌러서 오픈되었을 텐데 
    # 그럼 지뢰 말고 남은 0이 아닌 애들을 하나하나 클릭해야될 것
    # 그 남은 애들이 곧 전체에서 지뢰개수, 0인 개수, 오픈된 숫자 개수를 뺀 것과 같음
    # N*N - bombs_cnt - zeros_cnt, not_zero_cnt
    answer += (N*N - bombs_cnt - zeros_cnt - not_zero_cnt)

    print(f"#{tc} {answer}")