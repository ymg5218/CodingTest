// 4949
const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require('fs').readFileSync(file).toString().trim().split("\n");

const bracket = [["[", "]"], ["(", ")"]];

for (let i = 0; i < input.length - 1; i++) {
    let stack = [];
    const sentence = input[i];
    let isValid = true;
    for (let j = 0; j < sentence.length; j++) {
        if (sentence[j] === bracket[0][0] || sentence[j] === bracket[1][0]) {
            stack.push(sentence[j]);
        }
        else if (stack.length > 0 && sentence[j] === bracket[0][1]) {
            if (stack[stack.length - 1] === bracket[0][0]) {
                stack.pop();
            }
            else {
                isValid = false;
                break;
            }
        }
        else if (stack.length > 0 && sentence[j] === bracket[1][1]) {
            if (stack[stack.length - 1] === bracket[1][0]) {
                stack.pop();
            }
            else {
                isValid = false;
                break;
            }
        }
        else {
            if (sentence[j] === bracket[0][1] || sentence[j] === bracket[1][1]) {
                isValid = false;
            }
        }
    }
    if (stack.length === 0 && isValid) {
        console.log("yes");
    }
    else {
        console.log("no");
    }

}

