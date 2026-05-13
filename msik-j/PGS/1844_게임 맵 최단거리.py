from collections import deque

delta = [(1,0), (0,1), (-1,0), (0,-1)]

def solution(maps):
    N = len(maps)
    M = len(maps[0])
    visited = [[0]*M for _ in range(N)]
    
    q = deque()
    answer = -1 
    visited[0][0] = 1
    # r, c, 이동 칸수
    q.append((0,0,1))
    while q:
        cr, cc, moves = q.popleft()
        if cr == N-1 and cc == M-1:
            return moves

        for dir in range(4):
            nr, nc = cr+delta[dir][0], cc+delta[dir][1]
            if 0 <= nr and nr < N and 0 <= nc and nc < M and maps[nr][nc] == 1 and not visited[nr][nc]:
                visited[nr][nc] = 1
                q.append((nr, nc, moves+1))
            
    return answer

