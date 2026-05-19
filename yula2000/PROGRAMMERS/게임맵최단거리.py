# 우승 조건: 상대 진영에 더 빨리 가기
# 검: 막힘 흰: 갈 수 있음
# # 상대 진영에 도착할 수 없는 경우도 있음 -> -1반환
# # solution 함수 만들기

# 조건
# 맵: n*match
# 벽: 0 통로: 1
# 초기 캐릭터 위치 (1,1)
# 상대 캐릭터 위치(n,m)

# 변수가 안 주어져서 굉장히 당황...
# maps에 다 저장되어 있는 방식인가봄..?
# 델타 쓰기
# 저번주처럼 visited에 답 저장하면 될 듯

# from collections import deque

# dr = [1, -1, 0, 0]
# dc = [0, 0, -1, 1]
# visited = [[0]*n for _ in range(m)] 

# # 가로길이 
# n = len(maps[0])
# # 세로길이
# m = len(maps)


# def solution(r, c):
    # q = deque([r, c])

    # while q:
    #     cr, cc = q.popleft

    #     for dir in range(4):
    #         nr = cr + dr[dir]
    #         nc = cc + dc[dir]

    #         if 0 <= nr < n and 0 <= nr < n: # 가로 세로 체크
    #             if visited[nr][nc] == 0 and maps[nr][nc] == 0:
    #                 visited[nr][nc] = 1 
    

    # answer = 0
    # return answer

from collections import deque

def solution(maps):
    dr = [1, -1, 0, 0]
    dc = [0, 0, -1, 1]
    # visited = [[0]*n for _ in range(m)] 

    # 가로길이
    n = len(maps[0])
    # 세로길이
    m = len(maps)

    visited = [[0]*n for _ in range(m)] 

    # q = deque([r, c])
    q = deque()
    q.append((0,0))
    visited[0][0] = 1
    

    while q:
        cr, cc = q.popleft()


        for dir in range(4):
            nr = cr + dr[dir]
            nc = cc + dc[dir]

            if 0 <= nr < m and 0 <= nc < n: # 가로 세로 체크
                if visited[nr][nc] == 0 and maps[nr][nc] == 1:
                    visited[nr][nc] = visited[cr][cc] + 1
                    q.append([nr, nc])
    
    if visited[m-1][n-1] >= 1:
        return visited[m-1][n-1]
    else:
        return -1 
    # -1리턴 어디서 함?
    #가로세로 헷갈림
# print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))