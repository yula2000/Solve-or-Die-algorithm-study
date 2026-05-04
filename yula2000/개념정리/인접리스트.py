# input
# 7 8
# 0 1
# 0 2
# 0 5
# 0 6
# 3 4
# 3 5
# 4 5
# 4 6

# 그래프를 인접리스트로 표현하시오
# 연결된 정보만 저장

# 저장되는 방식 예시
# 0: [1, 2, 5, 6]
# 1: [...]
# 2: [...]

# v개의 노드만큼 비어있는 리스트로 시작
V, E = map(int, input().split())

graph = [[] for _ in range(V)]

for _ in range(E):
    start, end = map(int, input().split())
    graph[start].append(end)
    graph[end].append(start) # 양방향

print(graph)