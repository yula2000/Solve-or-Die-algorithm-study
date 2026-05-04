from collections import deque

def contact(cur_node):
    q = deque()

    # for next_node in graph[cur_node]: 
    #     q.append(next_node)

    #     while q:
    #         # sq  <- q
            # for _ in range(len(q)):
    #             next_node = q.popleft()
    #             if not visited[next_node]:
    #                 visited[next_node] = visited[cur_node] + 1
    #                 q.append(next_node)
    visited[cur_node] = 1

    q.append(cur_node)

    while q:
        now_node = q.popleft()
        # for _ in range(len(next_nodes)):
        for next_node in graph[now_node]:
        
            if not visited[next_node]:
                visited[next_node] = visited[now_node] + 1
                q.append(next_node)


T = 10
for tc in range(1, T+1):
    length, start = map(int, input().split())
    arr = list(map(int, input().split()))
 
    graph = [[] for _ in range(101)]  # 널널하게 100번 인덱스까지 만들었는데 이상적인 답이 궁금함
    # 윤우님: [] 안에 0을 넣으면 메모리를 덜씁니다.
    
    for i in range(0, length, 2):  # length+1 부터는 왜 인덱스 에러나는지 궁금함(length-1, -2 ... 해도 잘 됨)
        u, v = arr[i], arr[i+1]
        graph[u].append(v)

    # visited = [0 for _ in range(100)]
    visited = [0]*101

    contact(start)
    
    max_dist = max(visited)
    ans = 0
    for i in range(101):
        if visited[i] == max_dist:
            if i > ans:
                ans = i

    print(f"#{tc} {ans}")

    

    '''
    24 2
    100 17 39 22 100 8 100 7 7 100 2 7 2 15 15 4 6 2 11 6 4 10 4 2

    graph =
    [[], [], [7, 15], [], [10, 2], [], [2], [100], [], 
    [], [], [6], [], [], [], [4], [], [], [], [], [], [], [], 
    [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], 
    [], [22], [], [], [], [], [], [], [], [], [], [], [], [], [], 
    [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], 
    [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], 
    [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [17, 8, 7]] 
    '''