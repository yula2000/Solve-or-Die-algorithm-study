'''
[문제 요약]
모든 음식의 스코빌 지수 : k 이상
= 가장 맵지 않은 음식 스코빌 지수 + (두 번째로 맵지 않은 스코빌 지수*2)

모든 음식의 스코빌 지수를 k 이상으로 만들 수 없을 때 : -1

[개념]
- 힙이 뭐였지
    - 완전이진트리
    - 뭘 넣든 최솟값이 항상 맨 앞에 있도록 스스로 정렬을 유지하는 배열
    - heappush를 하면 힙 구조(정렬)로 자동 유지됨 => 재정렬 필요없음

[로직]
- for문 : 배열 내에 있는 스코빌 지수가 k 이상이 아닌지 확인
    - true : 배열 내에 있는 스코빌 지수 > k
        - scoville가 정렬이 되어 있으니까, scoville의 첫 번째 인덱스와 두 번째 인덱스
    - false : 배열 내에 있는 스코빌 지수 < k
        - return -1 

- 모든 음식의 스코빌 지수가 k 이상으로 만들 수 없을 경우 -1
    - 이미 모든 스코빌 지수가 k 이상일 때 

[오류난 점 / 의문점]
- for문을 사용했었는데 "모든 음식이 K 이상"이 될 때까지 반복해야하므로 while문 사용으로 변경함
- heappop을 사용할 때 scoville[i]처럼 인덱스로 접근하면 오류가 나고 scoville 배열 자체로 접근하기
- for문 또는 if문 으로 풀 수 있는가
'''

import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville) # 힙 정렬

    while scoville[0] < K:
        if len(scoville) < 2:   # 음식이 1개 남았을 때 <- 이거 생각 못 함
            return -1
        first_min = heapq.heappop(scoville)
        second_min = heapq.heappop(scoville)

        mix_scov = first_min + (second_min*2)
        heapq.heappush(scoville, mix_scov)
        answer += 1

    return answer

    