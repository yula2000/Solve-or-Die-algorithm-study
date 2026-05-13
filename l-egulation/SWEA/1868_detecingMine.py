'''
개 믿힌 ㄸㄹㅇ같은 문제를 봤나
진짜 얼마나 오래걸릴지 감도 안옴;

[생각정리]
일단 . 을 클릭하는데, 주위에 *가 있는 수 만큼 클릭한 부분을 그 숫자로 대체
주위에 *가 없어서 0이다? 그럼 인접한 .으로 퍼짐
> 이렇게 연쇄적으로 숫자 표시가 가능함 > 연쇄적인 부분은 클릭한 횟수에 포함 X
0이 아니라면 다시 클릭할 곳 탐색
그래서 최종적으로 area에서 모든 .을 숫자로 만들때까지의 최소 클릭 수 구하기

다른 그래프 문제처럼 시작점이 특정된 것이 아니므로 모든 .에서의 출발을 고려
그래서 area를 for문으로 돌면서 . 이면 bfs실행 > 한마디로 완탐?

[의문점]
의문점 1. 굳이 저렇게 모든 .에서의 경우를 다 따져야하나? bfs에서는 백트래킹이 안되나?
- 주변 지뢰가 0인 지점들만 먼저 찾아서 bfs 및 연쇄작용
- 백트래킹 X

의문점 2. 한 .을 클릭하고 연쇄적으로 숫자가 표시 됐을때,
다른 .을 클릭하는데 그때 남은 모든 .은 모두 후보?인데 거기서 효율적으로 선택하는 방법은?
- 주변 지뢰 개수를 모두 계산해두고, 거기서 주변 지뢰가 0인 부분들은 먼저 클릭하는 것이 가장 효율적

의문점 3. 마지막에 . 없는지 확인할때도 그럼 300x300을 for문으로 돌아야하나?더 효율적인 방법이 있지 않을까?
> 처음에 area에서 .의 개수를 세고, 나중에 .을 없애면서 숫자 0이 되면 끝?
- 어짜피 9만번 정도는 ㄱㅊ

[최종로직]
1. 맵을 스캔해서 미리 모든 칸에 대해 주변 지뢰개수 카운트
2. 1순위로 주변 지뢰개수 0인 칸을 클릭해서 연쇄작용을 일으켜 최대한 많은 칸을 터뜨림
3. 그 다음으로 연쇄작용으로도 안터진 칸을 클릭해서 나머지 다 터뜨림

최단 경로가 아니라 연쇄반응의 끝을 찾는?
'''
from collections import deque

# 8방향 탐색용 (상하좌우, 대각선까지)
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]

# 해당 칸 주위의 지뢰개수 카운트 함수
def mine_check(r, c):
    # 지뢰 개수
    mine_count = 0

    # 8방향 탐색하면서
    for dir in range(8):
        nr, nc = r + dr[dir], c + dc[dir]

        # area 범위 내에서
        if 0 <= nr < N and 0 <= nc < N:
            # 지뢰인거
            if area[nr][nc] == '*':
                # 지뢰 찾았으니까 지뢰 개수 +1
                mine_count += 1

    # 지뢰 개수 반환
    return mine_count

# 연쇄작용 bfs 함수
def chain_bfs(row, col):
    queue = deque([(row, col)])
    # 들어왔으니까 방문처리
    visited[row][col] = 1

    while queue:
        r, c = queue.popleft()

        # 현재 칸 주위의 지뢰 개수가 0이면?
        # > 이미 각 칸마다 주위 지뢰 개수를 카운트 해놔서 아래의 if문이 가능함
        if mine_count_area[r][c] == 0:
            # 8방향 주위 탐색
            for dir in range(8):
                nr, nc = r + dr[dir], c + dc[dir]

                if 0 <= nr < N and 0 <= nc < N:
                    # 방문하지 않았고, 지뢰가 아니라면
                    if not visited[nr][nc] and area[nr][nc] == '.':
                        # 방문 체크
                        visited[nr][nc] = 1
                        # 근데 옆 칸도 주변 지뢰 개수가 0개다?
                        # 그럼 얘도 queue에 넣어서 연쇄 작용
                        # > 결국 queue에는 연쇄작용이 되는 애들만 append함
                        if mine_count_area[nr][nc] == 0:
                            queue.append((nr, nc))

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    area = [list(map(str, input().strip())) for _ in range(N)]

    # 미리 맵을 스캔해서 모든 칸에 대해 주변 지뢰개수를 카운트
    mine_count_area = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            mine_count_area[i][j] = mine_check(i, j)

    visited = [[0]*N for _ in range(N)]

    # 최소 클릭 수
    min_click_count = 0

    # 먼저 주변 지뢰 개수가 0인 칸부터 터뜨림
    for i in range(N):
        for j in range(N):
            # 현재 칸이 지뢰가 아니고, 주변에 지뢰가 없으며, 방문하지 않은 칸이라면
            if area[i][j] == '.' and mine_count_area[i][j] == 0 and not visited[i][j]:
                # 바로 클릭
                min_click_count += 1
                # 그 후 연쇄작용
                chain_bfs(i, j)

    # 그리고 연쇄작용으로도 안터진 나머지 칸 카운트
    for i in range(N):
        for j in range(N):
            if area[i][j] == '.' and not visited[i][j]:
                min_click_count += 1
                # 방문처리만 해서 중복 방지
                visited[i][j] = 1

    print(f'#{tc} {min_click_count}')