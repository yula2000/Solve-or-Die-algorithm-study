import heapq
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [input() for _ in range(N)]
    dist = [[10**9] * N for _ in range(N)]
    dist[0][0] = 0
    q = []
    heapq.heappush(q, (0, 0, 0))
    while q:
        d, r, c = heapq.heappop(q)
 
        for i in range(4):
            if 0 <= r+dr[i] < N and 0 <= c+dc[i] < N:
                next_dist = int(arr[r+dr[i]][c+dc[i]]) + d
                if next_dist < dist[r+dr[i]][c+dc[i]]:
                    dist[r+dr[i]][c+dc[i]] = next_dist
                    heapq.heappush(q, (dist[r+dr[i]][c+dc[i]], r+dr[i], c+dc[i]))
    print(f'#{tc} {dist[N-1][N-1]}')
