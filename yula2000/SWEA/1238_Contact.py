# 문제
# 비상연락망과 연락을 시작하는 당번에 대한 정보가 주어질 때
#     1. 가장 나중에 연락 
#     2. 번호가 가장 큰 사람

# 각 정점은 개인
# 원 안의 숫자는 개인의 번호
# 빨간원은 연락 시작 당번
# 단방향 그래프
# 동시에 연락 -> bfs (근데 dfs도 되는거 아닌가?)
# 시간이 다 되어도 연락 못받는 사람도 있음 불쌍

# 제약 사항
# 부여번호 1부터 시작
# 중간에 비어있는 번호 존재 가능
# 다자 간 통화 가능
# 다시 연락 불가능

# 변수
# 테케 10개
# 테케 첫줄에는 데이터의 길이, 데이터의 시작점
# from to...제대로 읽을걸....


# 로직
# bfs로 풀라는 것 같지만 dfs로 풀고싶음 그렇게 풀거임
# 길이 저장해서 
# 1. 가장 길이가 긴거 일단 뽑기
# 2. 길이가 같다면 번호 큰거 뽑기
# 하수연이랑 토론해서 그렇게 풀면 개어려워진다는 것을 깨달음
# bfs
# visited 만들기

from collections import deque

for tc in range(1, 11):
    adj_arr = [[] for _ in range(101)] #비어있는 번호도 있고 암튼 복잡하니까 넉넉하게 최대인원수 +1로 근데 set() 쓰라는데 이해가 될 듯 안 될 듯
    data_length, start_v = map(int, input().split())
    data = list(map(int, input().split()))
    visited = [0]*101

    # 인접 리스트 구성
    for i in range(0, data_length ,2):
        start, end = data[i], data[i+1]
        adj_arr[start].append(end)

    # visited에 길이 저장    
    q = deque([start_v])
    visited[start_v] = 1 # 방문처리 반복문 안에다 넣지 말기

    while q:
        cur_v = q.popleft()

        for next_v in adj_arr[cur_v]:
            if visited[next_v] == 0:
                visited[next_v] = visited[cur_v] + 1
                q.append(next_v)

    key_val = max(visited)
    ans_lst = []

    for i in range(len(visited)): # 인데스 돌거니까 
        if visited[i] == key_val:
            ans_lst.append(i)

    ans = max(ans_lst)

    print(f'#{tc} {ans}')


