import heapq


T = int(input())
delta = [(0,1), (1,0), (0,-1), (-1,0)]

for tc in range(1, T+1):
    N = int(input())
    graph = [list(input()) for _ in range(N)]
    visited = [[-1]*N for _ in range(N)]

    q = [(0, 0, 0)]
    
    visited[0][0] = 0

    while q:
        now_time, now_r, now_c = heapq.heappop(q)
        if now_r == N-1 and now_c == N-1:
            break

        for dir in range(4):
            next_r, next_c = now_r+delta[dir][0], now_c+delta[dir][1]
            if 0 <= next_r < N and 0 <= next_c < N:
                next_time = now_time + int(graph[next_r][next_c])
                if visited[next_r][next_c] == -1 or visited[next_r][next_c] > next_time:
                    visited[next_r][next_c] = next_time
                    heapq.heappush(q, (next_time, next_r, next_c))
    
    print(f"#{tc} {now_time}")




# # 예전에 풀었던 풀이 (참고용 / DFS -> BFS(stack 활용))

# # DFS로 구현하려다 재귀 시간 초과로 안됨 -> BFS로 수정
# import sys
# sys.setrecursionlimit(10**6)
# def dfs(r, c, construct):
#     global answer
#     if r == N-1 and c == N-1:
#         if answer > construct:
#             answer = construct
#     for d in range(4):
#         nr, nc = r + dr[d], c + dc[d]
#         if 0<= nr < N and 0<= nc < N:
#             need_construct = int(maze[nr][nc])
#             if visited[nr][nc] == -1:
#                 visited[nr][nc] = construct + need_construct
#                 dfs(nr, nc, construct + need_construct)
#             else:
#                 if visited[nr][nc] < construct + need_construct:
#                     continue
#                 visited[nr][nc] = construct + need_construct
#                 dfs(nr, nc, construct + need_construct)


# BFS로 구현하기 로직은 비슷함
# from collections import deque

# def bfs(R, C):
#     global answer
#     stack = deque()
#     stack.append((R, C))
#     while stack:
#         r, c = stack.popleft()
#         construct = visited[r][c]
#         for d in range(4):
#             nr, nc = r +dr[d], c + dc[d]
#             if nr == N-1 and nc == N-1:
#                 if answer > construct:
#                     # 도착지는 0이므로 need construct 필요 x
#                     answer = construct
#                     # 도착했다면 다른 delta로는 도착할 수가 없으므로 break하고 while문 돌리기
#                     break
#             if 0<= nr < N and 0<= nc < N:
#                 need_construct = int(maze[nr][nc])
#                 if visited[nr][nc] == -1:
#                     visited[nr][nc] = construct + need_construct
#                     stack.append((nr, nc))
#                 else:
#                     if visited[nr][nc] <= construct + need_construct:
#                         continue
#                     visited[nr][nc] = construct + need_construct
#                     stack.append((nr, nc))


# # delta
# dr = [1, 0, -1, 0]
# dc = [0, 1, 0, -1]

# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     maze = [list(input()) for _ in range(N)]
#     # visited를 공사한 값으로 쓸 것이므로 -1로 채운다
#     visited = [[-1]*N for _ in range(N)]
#     # 시작할 땐 공사한 값이 0
#     visited[0][0] = 0
#     # 최솟값을 구해야 하므로 무한대로 설정
#     answer = float('inf')
#     bfs(0, 0)
#     print(f"#{tc} {answer}")