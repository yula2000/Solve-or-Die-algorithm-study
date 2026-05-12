from collections import deque

def bfs(start, maps):
    n = len(maps)
    m = len(maps[0])

    start_r, start_c = start
    queue = deque([(start_r, start_c)])

    visited = [[0]*m for _ in range(n)]
    visited[start_r][start_c] = 1

    depth = 1

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            if r == n - 1 and c == m - 1:
                return depth

            for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                nr, nc = r + dr, c + dc

                if (0 <= nr < n and 0 <= nc < m) and maps[nr][nc] == 1:
                    if not visited[nr][nc]:
                        visited[nr][nc] = 1
                        queue.append((nr, nc))

        depth += 1

    return -1

def solution(maps):
    answer = bfs((0, 0), maps)
    return answer