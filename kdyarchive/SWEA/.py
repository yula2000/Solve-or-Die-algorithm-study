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