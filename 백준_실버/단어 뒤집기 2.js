// 17413
const file = process.platform === "linux" ? "dev/stdin" : "./input.txt";
const input = require("fs").readFileSync(file).toString().trim();

let result = "";
let stack = [];
let isOpened = false;
for (let i = 0; i < input.length; i++) {
    if (isOpened === true) {
        result += input[i];
        if (input[i] === ">") {
            isOpened = false;
        }
    }
    else {
        if (input[i] === " ") {
            while (stack.length > 0) {
                result += stack.pop();
            }
            result += " ";
        }
        else {
            if (input[i] === "<") {
                isOpened = true;

                while (stack.length > 0) {
                    result += stack.pop();
                }

                result += input[i];
            }
            else {
                stack.push(input[i]);
            }
        }

    }
}

while (stack.length > 0) {
    result += stack.pop();
}

console.log(result);
