import heapq

dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]

def cheapest(time, r, c):
    pq = []
    visited[r][c] = 1
    heapq.heappush(pq, (time, r, c))

    while pq:
        total_time, cr, cc = heapq.heappop(pq)

        if cr == cc == N-1:
            return total_time
        
        for i in range(4):
            nr = cr + dir[i][0]
            nc = cc + dir[i][1]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                visited[nr][nc] = 1
                heapq.heappush(pq, (total_time + arr[nr][nc], nr, nc)) 
                # pq안에 힙푸시할때 total_time에 누적하지 않았어서 도착점의 값인 0만 출력하고 있었음

T = int(input())
for C in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    answer = cheapest(arr[0][0], 0, 0)  # (0, 0, 0) > 시작점 가중치가 0이 아닐 수 있음
    print(f"#{C} {answer}")

#===============================================================#

from collections import deque

dir = [(0, -1), (0, 1), (-1, 0), (1, 0)]  # dir[i][0], dir[i][1]

def cheapest(r, c, time):
    q = deque()
    visited[r][c] = 1
    q.append(((r, c), time))

    while q:
        (cr, cc), time = q.popleft()

        if cr == cc == N-1:
            return time
        
        pq = []
        for i in range(4):
            nr = cr + dir[i][0]
            nc = cc + dir[i][1]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                pq.append((nr, nc))

            # next_r = 9
            # next_c = 9
            time_add = 9
            for j in range(len(pq)):
                jr, jc = pq[j][0], pq[j][1]

                # if 0 <= jr < N and 0 <= jc < N and not visited[jr][jc]:
                # if jr <= next_r: next_r = jr
                # if jc <= next_c: next_c = jc

                # if arr[jr][jc] <= time_add:
                #     time_add = arr[jr][jc]
                time_add = min(arr[jr][jc], time_add)

            # visited[next_r][next_c] = 1
            # q.append(((next_r, next_c), time+arr[cr][cc]))
                visited[jr][jc] = 1
                q.append(((jr, jc), time + time_add))


T = int(input())
for C in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    visited = [[0]*N for _ in range(N)]

    answer = cheapest(0, 0, 0)
    print(f"#{C} {answer}")

# S = arr[0][0]
# G = arr[N-1][N-1]

# S부터 G까지 가는데 누적합이 가장 적은 경로 선택
# 한 depth 마다 계속 작은 숫자만 고르면 되는거 아닌가?
# 델타, 방문 안 한 곳이면서 가중치가 가장 작은걸 고르는 bfs(다익스트라)
# 지금 코드로 풀 수 없는 이유: 그리디의 오류