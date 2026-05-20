import heapq

def solve(arr,start,end):
    N = len(arr)
    visited = [[False] * N for _ in range(N)]
    heap = []
    heapq.heappush(heap, (arr[0][0], start))
    visited[0][0] = True

    while heap:
        cost, (x,y) = heapq.heappop(heap)

        if (x,y) == end:
            return cost

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = True
                heapq.heappush(heap, (cost + arr[nx][ny], (nx, ny)))


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    start = (0, 0)
    end = (N-1, N-1)    


print(f"#{tc} {solve(arr, start, end)}")

