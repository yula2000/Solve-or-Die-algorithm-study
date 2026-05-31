

# 리스트에서 가장 큰 수를 찾아 n의 값을 1씩 빼는 방식

# work = [4,3,3] , n = 4 라고 하면 4에서 1을 빼고 그다음 가장 큰 수인 3에서 1을 빼는 방식으로 진행

# 그리고 n이 0이 되면 혹은 work의 값들이 0이 되면 해당 리스트에 있는 값들의 제곱의 합을 구하는 방식

def solution(n, works):
    
    while n > 0:
        if max(works) == 0:
            break
            
        max_num = max(works)
        max_idx = works.index(max_num)
        works[max_idx] -= 1
        n -= 1
        
    box = []
    for x in works:
        box.append(x**2)
        
    answer = sum(box)
    return answer