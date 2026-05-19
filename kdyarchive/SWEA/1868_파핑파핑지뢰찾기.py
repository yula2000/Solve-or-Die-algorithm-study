from collections import deque

dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, 1, 1, 1, 0, -1, -1, -1]


def popping(start_r, start_c):
    q = deque()
    # visited[start_r][start_c] = 'C'  # 처음 시작한 곳은 C로 표시하기/덮어씌워질거지만 while문 시작을 위해
    q.append((start_r, start_c))
    visited[start_r][start_c] = 1

    while q:
        current_r, current_c = q.popleft()

        # # 현재 위치가 지뢰라면 게임 끝
        # if arr[current_r][current_c] == '*':
        #     return '끝'  # 근데 애초에 큐에 지뢰 아닌걸 넣으면 이 경우가 생길 수 있나?
        # 근데 지뢰가 어디있는지 다 보이니까 굳이 안 넣어도 될 조건인듯

        for dir in range(8):
            next_r = current_r + dr[dir]
            next_c = current_c + dc[dir]

            if 0 <= next_r < N and 0 <= next_c < N:
                # 다음 방향에 지뢰가 있다면: 카운트만 하고 큐에 넣지 말기
                if arr[next_r][next_c] == '*':
                    bomb_count[current_r][current_c] += 1  # 현재 위치에 개수 덮어쓰기
                # # 지뢰말고 그냥 길이라면: 큐에만 넣기
                # elif arr[next_r][next_c] == '.':
                #     q.append((next_r, next_c))
                
        # 8방향 다 보고 지뢰 셌는데 0인경우에만 다음 방향들 큐에 넣기
        if bomb_count[current_r][current_c] == 0:
            for dir in range(8):
                next_r = current_r + dr[dir]
                next_c = current_c + dc[dir]
                q.append((next_r, next_c))

        # 현재 위치에 1 이상이 찍히면 종료
        # elif visited[current_r][current_c] > 0:
        else:
            return '클릭횟수'


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    # for i in range(N):
    #     arr = list(input())
    arr = []
    for i in range(N):
        arr.append(list(input()))

    # visited = arr[:]
    visited = [[0]*N for _ in range(N)]  # 방문체크용
    bomb_count = [row[:] for row in arr]  # 클릭한 위치에 지뢰 개수 기록용


    for r in range(N):
        for c in range(N):
            if bomb_count[r][c] == '.':
                popping(r, c) 
            
            

    


'''
1. arr을 2차원리스트로 받기 -> N개의 행 반복, N개의 데이터
2. 배열을 순회하면서 이전 값과 비교 
    -> 임시값을 정해두고 [0][0]~[N-1][N-1]까지 값 비교
    -> 값: [r][c]에서 클릭을 시작했을때, bfs가 끝날때까지 클릭한 횟수
3. bfs
    -> 인접한 8방향의 값들을 큐에 넣고
    -> 지뢰 개수를 현재 위치에 표시
    -> 범위체크 + 지뢰는 visited만 표시하고 큐에 넣지 않기/나머지는 큐에도 넣고 방문표시도하기
        -> visited 배열에 지뢰의 개수도 세는게 좋을까?

2 & 3 => 반복문안에서 r, c 지정해주기 

==============
1. 지뢰를 클릭하면 게임 끝 -> 클릭==현재위치

1. 파핑파핑 함수 안:
    1) 시작하는 위치 == 클릭 / C로 표시
    2) 주변 8방향 탐색
        1. 지뢰가 아예 없는 경우
            - 8방향의 칸도 자동으로 숫자 표시(큐에 넣기?)
            - 현재 위치에 0이 찍히면 8방향 계속 큐에 넣기
        2. 지뢰가 한개 이상 있는 경우 
            - 종료

'''