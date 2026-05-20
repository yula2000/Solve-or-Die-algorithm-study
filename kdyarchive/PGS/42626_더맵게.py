answer = -1

def mix(scoville, K, count_mix):
    global answer
    
# 현재 리스트를 순회하며 K 이상인지 확인
    count_k = 0
    for i in range(len(scoville)):
        if scoville[i] >= K:
            count_k += 1

    if count_k == len(scoville):
        answer = count_mix
        return 

    sorted_list = sorted(scoville) # , reverse=True
    x = sorted_list.pop(0)  # 첫번째로 작은 값
    # y = sorted_list.pop(1)  # 두번째로 작은 값
    y = sorted_list.pop(0)  # x를 pop하고 나면 이미 인덱스가 한 칸씩 당겨졌기때문에 1번을 뽑으면 원하는 값이 뽑히지 않음

    z = x + y*2  # 공식 적용해서 다시 리스트에 넣기
    sorted_list.append(z)

    mix(sorted_list, K, count_mix+1)
    return
    
# 재귀함수 호출   
def solution(scoville, K):
    global answer
    
    answer = -1
    
    mix(scoville, K, 0)
    return answer


# 모든 값이 K이상이 될때까지 **반복**
# 1,2등 뽑기
    # 오름차순 정렬 > [0]이 1등, [1]이 2등
    # x = pop(0), y = pop(1)
# 공식 적용
    # x + y*2
    # 위에 계산한 값을 리스트에 append 다시 하기
    # count += 1
