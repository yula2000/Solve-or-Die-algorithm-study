from collections import deque

def solution(maps):
    answer = 0
    r = len(maps)
    c = len(maps[0])
    visited = [[0] * c for _ in range(r)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    start = (0, 0)
    visited[0][0] = 1
    q = deque()
    q.append(start)
    while q:
        pr, pc = q.popleft()
        for i in range(4):
            nr = pr+dr[i]
            nc = pc+dc[i]
            if 0 <= nr < r and 0 <= nc < c:
                if visited[nr][nc] > 0 or maps[nr][nc] == 0:
                    continue
                q.append((nr, nc))
                visited[nr][nc] = visited[pr][pc] + 1
    answer = visited[r - 1][c - 1]
    if answer > 0:
        return answer
    else:
        return -1
