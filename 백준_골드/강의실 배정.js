// 11000

class Heap {
    constructor() {
        this.hq = [null];
    }

    size() {
        return this.hq.length - 1;
    }

    swap(x, y) {
        [this.hq[x], this.hq[y]] = [this.hq[y], this.hq[x]];
    }

    peek() {
        return this.hq[1];
    }

    heappush(x) {
        this.hq.push(x);

        let idx = this.size();
        let parent_idx = Math.floor(idx / 2);

        while (idx > 1 && this.hq[idx] < this.hq[parent_idx]) {
            this.swap(idx, parent_idx);
            idx = parent_idx;
            parent_idx = Math.floor(idx / 2);
        }
    }

    heappop() {
        if (this.size() <= 1) {
            this.hq.pop();
        }

        this.hq[1] = this.hq.pop();

        let idx = 1;
        let left_idx = idx * 2;
        let right_idx = idx * 2 + 1;

        while (
            (this.hq[left_idx] && this.hq[left_idx] < this.hq[idx])
            ||
            (this.hq[right_idx] && this.hq[right_idx] < this.hq[idx])
        ) {
            if (this.hq[right_idx] && this.hq[right_idx] < this.hq[left_idx]) {
                this.swap(idx, right_idx);
                idx = right_idx;
            }
            else if (this.hq[left_idx] && this.hq[left_idx] < this.hq[right_idx]) {
                this.swap(idx, left_idx);
                idx = left_idx;
            }
        }
    }
}

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(file).toString().trim().split("\n");


const N = parseInt(input.shift().trim());
const timeLine = input.map(value => value.trim().split(' ').map(Number));

timeLine.sort((a, b) => a[0] - b[0]);


const heapq = new Heap();

let max_room = 0;
for (let idx = 0; idx < N; idx++) {
    let start_time = timeLine[idx][0];
    let end_time = timeLine[idx][1];
    if (heapq.size() > 0 && heapq.peek() <= start_time) {
        heapq.heappop();
    }
    heapq.heappush(end_time);
    max_room = Math.max(max_room, heapq.size());
}

console.log(max_room);

