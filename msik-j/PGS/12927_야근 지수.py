import heapq
def solution(n, works):
    remain_works = []
    # max heap을 위해 음수로 push
    for work in works:
        heapq.heappush(remain_works, -work)
    
    for _ in range(n):
        # 중간에 남은 작업량이 없으면 피로도는 0
        if not remain_works:
            return 0
        temp = heapq.heappop(remain_works)

        # 작업량이 0이면 그냥 없애버리면 됨
        if temp+1 == 0:
            continue
        # 음수 값이 나왔으므로 일을 한다 쳤을 때 +1 해주는 개념(-(-1))
        heapq.heappush(remain_works, temp+1)
    
    answer = 0
    # remain_works에 남은 애들을 다 pop하고 제곱해서 더하기
    while remain_works:
        answer += (remain_works.pop())**2
    return answer