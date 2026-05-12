from collections import deque
import pprint
dr = [0, 1, 1, 1, 0, -1, -1, -1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    map = []
    for i in range(N):
        map.append(input())
    visited = [[0] * N for _ in range(N)]
    for r in range(N):
        for c in range(N):
            if map[r][c] == '*':
                visited[r][c] = -1
                continue
            count = 0
            for i in range(8):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < N and 0 <= nc < N:
                    if map[nr][nc] == '*':
                        count += 1
            visited[r][c] = count
    answer = 0
    q = deque()
    for r in range(N):
        for c in range(N):
            if visited[r][c] != 0:
                continue
            answer += 1
            visited[r][c] = -1

            q.append((r, c))
            while q:
                pr, pc = q.popleft()
                for i in range(8):
                    nr = pr + dr[i]
                    nc = pc + dc[i]
                    if 0 <= nr < N and 0 <= nc < N:
                        if visited[nr][nc] == 0:
                            visited[nr][nc] = -1
                            q.append((nr, nc))
                        elif visited[nr][nc] != -1:
                            visited[nr][nc] = -1

    for r in range(N):
        for c in range(N):
            if visited[r][c] != -1:
                answer += 1
    print(f'#{tc} {answer}')