'''
섞는 함수 정의
> 함수 실행될 때 마다 answer += 1
> 그리고 return

scoville을 정렬하고 idx = 0, 1 골라서 섞는 함수에 넣으면 되는거 아님?
> 그럼 heap 사용하면 편할듯

-1 예외처리 까먹어서 2번 틀림
'''
from heapq import heappop, heappush

# 가장 낮은 수와 그 다음으로 낮은 수를 섞는 함수
def mix(char1, char2):
    result = char1 + (char2 * 2)
    return result

def solution(scoville, K):
    # heapqueue 만들기
    pq = []

    # 기존 리스트를 heapqueue로 바꿈
    for num in scoville:
        heappush(pq, num)

    answer = 0

    # heapqueue의 가장 작은수가 K 이상이면 while문 종료
    while pq[0] < K:
        # 예외처리
        # > heapqueue의 길이가 2보다 작으면, 즉 1이면 pop을 2번 못함
        # >> IndexError남
        # >> 그래서 아래와 같이 예외 처리해서 -1 return
        if len(pq) < 2:
            return -1

        # 가장 작은 수, 그 다음으로 작은 수 뽑아서
        char1 = heappop(pq)
        char2 = heappop(pq)

        # 섞어서 나온 새로운 요소 heapqueue에 push
        new_char = mix(char1, char2)
        heappush(pq, new_char)

        # 섞기 횟수 +1
        answer += 1

    # 여기까지 오면 예외 처리 안걸렸으므로 섞기 횟수 return
    return answer