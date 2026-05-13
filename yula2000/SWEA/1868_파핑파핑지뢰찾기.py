# 처음 풀이
# # R*C 크기 표
# # 지뢰칸 선택하면 소리
# # 지뢰 없는 칸이면 맞 닿아 있는 칸에 최대 몇개의 지뢰가 있는지 숫자로 표시
# # 숫자 0일 때: 8칸에도 숫자 표시 -> BFS인데 숫자 표시하면서 가기
# 지뢰 있는 칸 제외한 모든 칸의 숫자 표시 목표

# # 주어진 수
# # 첫줄:  테케 수
# # 두번째 줄 : N(표 크기)
# # N개의 줄 동안 문자열
# # * = 지뢰
# # . = 지뢰 없음

# # 필요한 거
# # 8방향 탐색

# from collections import deque
# dr = [-1, -1, -1, 0, 0, 1, 1, 1]
# dc = [-1, 0, 1, -1, 1, -1, 0, 1]


# T = int(input())

# for tc in range(1, T+1):
#     N = int(input())
#     arr = [list(input()) for _ in range(N) ]
#     visited = [[0] for _ in range(N)]
#     ans = 0 #초기값
#     # 모든 칸을 돌면서 주변 지뢰 개수 파악 
#     for r in range(N):
#         for c in range(N):
#             if arr[r][c] == '*':
#                 visited[r][c] = -1 # 지뢰는 -1로 표시
#                 continue
#             else:

#     # bfs 처리 로직
#     # 연쇄 반응?

#     print(f'#{tc} {ans}')



from collections import deque

dc = [-1, -1, -1, 0, 0, 1, 1, 1]
dr = [-1, 0, 1, -1, 1, -1, 0, 1]

def bfs(r, c):
    q = deque([(r, c)])
    visited[r][c] = True
    
    while q:
        cr, cc = q.popleft()
        
        # 8방향 탐색
        for dir in range(8):
            nr = cr + dr[dir]
            nc = cc + dc[dir]
            
            # 범위 안에 있고 방문 안하고 지뢰가 아닌 칸이면 방문처리
            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc] and arr[nr][nc] != '*':
                visited[nr][nc] = True

                # 지뢰 없는 칸이면 q에 넣기
                if mine_counts[nr][nc] == 0:
                    q.append((nr, nc))

T = int(input())
for tc in range(1, T + 1):

    N = int(input())

    arr = [list(input()) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    # 주변 지뢰 개수를 미리 저장할 배열
    mine_counts = [[0] * N for _ in range(N)]
    
    # 모든 칸 돌면서 지뢰 개수 세기
    for r in range(N):
        for c in range(N):
            # 만약 지뢰칸이면 계산할 필요 없으니까 그냥 넘어가
            if arr[r][c] == '*':
                continue
            # 초기값
            count = 0
            for dir in range(8):
                nr = r + dr[dir]
                nc = c + dc[dir]
                # 다음칸이 지뢰면 지금칸에 +=1
                if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == '*':
                    count += 1
            # 주변칸 지뢰개수 저장
            mine_counts[r][c] = count

    # 답 초기값    
    ans = 0
    
    # 모든 칸 돌면서 지뢰칸이 아니고 주변에 지뢰가 없고 방문하지 않은 칸 가서 답에 +=1 해주고 bfs실행
    # 0인 칸 우선적으로 터뜨려야 최소 클릭임
    for r in range(N):
        for c in range(N):
            if arr[r][c] != '*' and mine_counts[r][c] == 0 and not visited[r][c]:
                ans += 1
                bfs(r, c)

    # 0인 칸 다 터뜨려도 안 열린 칸 클릭   
    for r in range(N):
        for c in range(N):
            if arr[r][c] != '*' and not visited[r][c]:
                ans += 1
                
    print(f"#{tc} {ans}")