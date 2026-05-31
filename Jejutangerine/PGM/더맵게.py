

import heapq

def makespicy(scoville, K):
    heapq.heapify(scoville)

    cnt = 0
    while scoville[0] < K:
        if len(scoville)<2:
            return -1
        
        first  = heapq.heappop(scoville)
        second = heapq.heappop(scoville)

        new_food = first + (second*2)
        
        heapq.heappush(scoville, new_food)
        cnt+=1
    return cnt

scoville = list(map(int,input().split()))
K = int(input())

print(makespicy(scoville,K))