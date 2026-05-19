import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        food_1 = heapq.heappop(scoville)
        if food_1 >= K:
            return answer

        if len(scoville) == 0:
            return -1
        
        food_2 = heapq.heappop(scoville)
        new_food = food_1 + (food_2*2)
        heapq.heappush(scoville, new_food)
        answer += 1
    