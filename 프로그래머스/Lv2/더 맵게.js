/**
 * 힙 구조
 *              1
 *          2       3
 *       4     5  6    7       
 * - 왼쪽 자식 인덱스 = 부모 인덱스 * 2
 * - 오른쪽 자식 인덱스 = 부모 인덱스 * 2 + 1
 * - 부모 인덱스 = Math.floor(자식 인덱스 / 2)
 * 
 */
class MinHeap {
    constructor() {
        // 0번째 인덱스는 더미 인덱스
        this.hq = [null];
    }
    // 힙의 사이즈를 return
    size() {
        return this.hq.length - 1;
    }
    // x 노드와 y 노드를 서로 바꿈
    swap(x, y) {
        [this.hq[x], this.hq[y]] = [this.hq[y], this.hq[x]];
    }
    // 최소값을 return
    peek() {
        return this.hq[1];
    }
    /**
     * 삽입 연산 로직
     * 1. hq의 마지막 위치에 요소 추가 -> hq.push()
     * 2. 초기 위치에서부터, 부모 노드와 새로 추가된 노드의 값을 비교하며, 새로 추가된 값이 부모 노드 값보다 작다면 둘의 위치를 교환한다.
     * 3. 추가된 노드 값이 부모 노드보다 클 때까지 반복한다.
     */
    heappush(x) {
        this.hq.push(x) // 1

        let idx = this.size(); // 2 ~ 3
        let parent_idx = Math.floor(idx / 2);
        while (idx > 1 && this.hq[idx] < this.hq[parent_idx]) {
            this.swap(idx, parent_idx);
            idx = parent_idx;
            parent_idx = Math.floor(idx / 2);
        }
    }

    /**
     * 삭제 연산 로직
     * 1. hq에서 가장 작은 값인 루트 노드를 제거한다. 그리고 hq의 마지막 요소를 루트로 이동시킨다.
     * 2. 새로운 루트 노드와 자식 노드의 값을 비교하며, 자식 노드의 값이 작다면 루트 노드의 위치를 교환한다.
     * 3. 자식 노드의 값이 더 클 때까지 반복한다.
     */
    heappop() {
        // 힙의 크기가 1이라면 null과 root만 존재한다는 뜻.
        if (this.size() <= 1) {
            return this.hq.pop();
        }

        const value = this.hq[1]; // 1
        this.hq[1] = this.hq.pop();

        let idx = 1; // 2
        let left_idx = idx * 2;
        let right_idx = idx * 2 + 1;

        // 왼쪽 자식 노드가 존재하면서 값이 부모 노드보다 작거나
        // 오른쪽 자식 노드가 존재하면서 값이 부모 노드보다 작은 경우 계속 수행
        while ( // 3
            (this.hq[left_idx] && this.hq[left_idx] < this.hq[idx])
            ||
            (this.hq[right_idx] && this.hq[right_idx] < this.hq[idx])
        ) {
            // 더 작은 자식 노드와 교체
            if (this.hq[right_idx] && this.hq[right_idx] < this.hq[left_idx]) {
                this.swap(idx, right_idx);
                idx = right_idx
            }
            else {
                this.swap(idx, left_idx);
                idx = left_idx
            }
            left_idx = idx * 2;
            right_idx = idx * 2 + 1;
        }

        return value;

    }
}

function solution(scoville, K) {
    var answer = 0;

    const hq = new MinHeap();

    scoville.forEach((s) => {
        hq.heappush(s);
    });

    while (hq.size() >= 2 && hq.peek() < K) {
        const minimum_1 = hq.heappop();
        const minimum_2 = hq.heappop();
        hq.heappush(minimum_1 + minimum_2 * 2);
        answer += 1;

    }

    if (hq.peek() < K) {
        return -1;
    }

    return answer;
}

console.log(solution([1, 2, 3, 9, 10, 12], 7))