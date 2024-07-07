// 2606

const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(file).toString().trim().split('\n');

const N = parseInt(input[0].trim());

const graph = Array.from(Array(N + 1), () => new Array());
const visited = new Array(N + 1).fill(false);

for (let i = 2; i < input.length; i++) {
    let [v1, v2] = input[i].trim().split(' ').map(Number);
    graph[v1].push(v2);
    graph[v2].push(v1);
}

function bfs() {
    const queue = [];

    let cnt = 0;

    queue.push(1);
    visited[1] = true;

    while (queue.length > 0) {
        const now_v = queue.shift();

        graph[now_v].forEach(next_v => {
            if (!visited[next_v]) {
                visited[next_v] = true;
                queue.push(next_v);
                cnt++;
            }
        });
    }

    return cnt;
}

console.log(bfs());



