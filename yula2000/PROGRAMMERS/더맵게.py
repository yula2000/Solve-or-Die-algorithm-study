#------------------------------------------------------------------------
# 우선순위 큐는 힙 이용해서 구현
# 힙(구현 방법): 
# - 완전이진트리 형태
# - 부모 노드 값이 항상 자식 노드들의 값보다 크거나, 작아야함(max/mini heap)
# - 배열 이용해 구현
# - 트리 노드에 번호 붙임 여기서 번호 == 인덱스


# 우선순위 큐(개념):
# - 각 원소들은 우선순위 가지고 있음 
# - 높은 우선순위 가진 원소가 먼저 처리, 같은 우선순위라면 먼저 들어온 원소 우선 처리

# 사용법
# import heapq
# from queue import PriorityQueue
# heappop은 힙에서 최솟값을 꺼내는 함수
# heappush는 힙에 값을 넣는 함수

# q = PriorityQueue() 
# q1 = PriorityQueue(maxsize=10) # maxsize를 활용하면 크기 제한 가능

# 문제
# 모든 음식의 스코빌 지수를 k이상으로 만들기 
# 스코빌 지수가 가장 낮은 두 음식 섞어서 새로운 음식 만들기
#     방법: 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

# 스코빌 지수를 담은 배열: scoville
# 원하는 스코빌 지수 == K 
# 모든 음식의 스코빌 지수를 K 이상으로 만들기 위한 최소 회수를 구하기

# 제약 조건
# 2 <= 스코빌 길이 <= 1,000,000 
# 만약 모든 음식 섞어도 k이상으로 못 만들면 -1 return

# 로직
# 계속 가장 작은 두 값을 꺼내서 섞는거니까 -> mini heap 사용
#------------------------------------------------------------------------

# import heapq
# scoville = [10, 7, 5]	
# heapq.heapify(scoville)
# print(scoville)

# 힙정렬되는 거 보고싶어서 뽑아봄
# 처음에 막 섞여도 힙정렬되는 줄 알았는데 힙의 규칙은 "부모 ≤ 자식" 이 조건 때문에 정렬되어야 실행되는 거 였음ㅡㅡ
# 그래서 또다른 의문이 생김 heapq는 mini heap만 되는데 max heap은 어떻게 구현하지?
#     import heapq

# scoville = [1, 2, 9, 3, 10, 12]

# # 전부 음수로 변환해서 넣기
# heap = [-x for x in scoville]
# heapq.heapify(heap)

# # 꺼낼 때 다시 음수로 변환
# while heap:
#     print(-heapq.heappop(heap))  # 12, 10, 9, 3, 2, 1 순서로 출력
#------------------------------------------------------------------------
import heapq

def solution(scoville, K):
    # scoville = [1, 2, 3, 9, 10, 12]
    # K = 7

    # 스코빌 리스트 힙으로 만들어주기..?
    heapq.heapify(scoville)

    answer = 0

    # 문제 조건에서 k이상으로 만들라고 했으니까 k보다 작으면 반복하고 k보다 같거나 커지면 중단
    while scoville[0] < K:

        # 처음에 하나도 안되는 거 조건 이렇게 주고싶었는데 섞을 떄 두번째 스코빌지수에 *2 때문에 반례 나올 수도 있어서 안됐음 
        # 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
        # if sum(scoville) < k:
        #     return -1

        if len(scoville) <= 1:
            return -1
        
        # 제일 앞에 있는 애 나옴
        first_food = heapq.heappop(scoville)
        # 앞에서 두번째 나옴
        second_food = heapq.heappop(scoville)
        # 공식에 따라 새로운 음식 만들어주기
        new_food = first_food + second_food * 2
        # 스코빌에 새로운 음식 만들어주기
        heapq.heappush(scoville, new_food)

        answer += 1
        

    return answer