# 문제 조건
# 정점: N 간선: M 
# 무방향, 가중치 없음
# 최장 경로의 길이 구하기

# 변수
# 첫줄: T
# 두개의 자연수: N, M
# 다음줄부터 M개의 줄에 걸쳐서 간선 정보를 나타내는 두 정수가 주어짐
# 정점 번호 1 부터 시작

# 로직
# 인접리스트 받기(정점 번호 주의)
# dfs로 탐색 
#     visited배열 사용하기
#     초기값 세팅해서 더 많은 수의 경로가 나오면 갱신
# + 모든 경로 탐색해서 리스트에 저장 후 최대 길이 max로 찾기


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    # 정보 받을 인접리스트 만들어놓기 정점 번호 1부터 시작하니까 범위에 +1
    arr = [[] for _ in range(N+1)]
    visited = [0] * (N+1) # 처음에 대괄호 하나 더 쳐서 인덱스 에러남 주의하기!
    ans = 0 # 초기값

    for _ in range(M):
        start, end = map(int, input().split())
        arr[start].append(end)
        arr[end].append(start)
    # print(arr)

    def dfs(cv, length):
        global ans

        if length > ans:
            ans = length
        
        for nv in arr[cv]:
            if visited[nv] == 0: # 만약 다음 정점 방문 안했으면
                visited[nv] = 1 # 방문도장
                dfs(nv, length+1) # 재귀호출
                visited[nv] = 0 # 분기점 돌아왔을 때를 위해 도장 지우기
    # 시작점            
    for i in range(1, N + 1):
        visited[i] = 1
        dfs(i, 1) # 테케에서 간선 하나도 없어도 1 나왔음
        visited[i] = 0 # 이거 없어서 처음에 틀림

    print(f'#{tc} {ans}')