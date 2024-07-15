import heapq

def solution(operations):
    answer = []

    maxHeap = []
    minHeap = []
    nowLength = 0
    for _op in operations:
        op = _op.split(' ')
        if op[0] == "I":
            heapq.heappush(minHeap, int(op[1]))
            heapq.heappush(maxHeap, int(op[1]) * -1)
            nowLength += 1
        else:
            if nowLength > 0:
                if op[1] == "-1":
                    heapq.heappop(minHeap)
                    nowLength -= 1
                else:
                    heapq.heappop(maxHeap) * -1
                    nowLength -= 1
        
        # 실제 큐 길이가 0이면 둘 다 초기화
        if nowLength <= 0:
            maxHeap.clear()
            minHeap.clear()

    if nowLength <= 0:
        return [0, 0]
    else:
        answer.append(heapq.heappop(maxHeap) * -1)
        answer.append(heapq.heappop(minHeap))
        return answer

if __name__ == "__main__":
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))