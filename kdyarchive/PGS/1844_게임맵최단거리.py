from collections import deque

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

    
def solution(maps):
    
    n = len(maps[0])
    m = len(maps)
    
    visited = [[0]*n for _ in range(m)]
    
    start_r, start_c = 0, 0
    
    q = deque()
    q.append((start_r, start_c))
    visited[start_r][start_c] = 1
    
    while q:
        current_r, current_c = q.popleft()
        
        if current_r == m-1 and current_c == n-1:
            answer = visited[m-1][n-1]
            return answer
        
        for dir in range(4):
            next_r = current_r + dr[dir]
            next_c = current_c + dc[dir]
            
            if 0 <= next_r < m and 0 <= next_c < n:
                if not visited[next_r][next_c] and maps[next_r][next_c] == 1:
                    q.append((next_r, next_c))
                    visited[next_r][next_c] = visited[current_r][current_c] + 1
                    
    return (-1)