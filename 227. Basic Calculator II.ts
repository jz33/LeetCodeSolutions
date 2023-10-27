/*
227. Basic Calculator
https://leetcode.com/problems/basic-calculator-ii/
Only consider '+', '-', '*', '/', numbers
*/
function compute(num: number, op: string, stack: number[]) {
    // For '*', '/', compute current num with previous num.
    // For '+', '-', not compute but push the value to the stack,
    // in case there is a '*', '/' following up.
    if (op === '+') {
        stack.push(num);
    } else if (op === '-') {
        stack.push(-num);
    } else if (op === '*') {
        stack.push(stack.pop()! * num);
    } else if (op === '/') {
        const r = stack.pop()! / num;
        if (r > 0) {
            stack.push(Math.floor(r));
        } else {
            stack.push(Math.ceil(r));
        }
    }
}

function calculate(s: string): number {
    const ops = ['+', '-', '*', '/'];
    let op = '+';

    // A stack that saves previous numbers
    const stack: number[] = [];
    // Represents current number in parsing
    let num = 0;

    for (const char of s) {
        const digit = parseInt(char);
        if (!isNaN(digit)) {
            num = num * 10 + digit;
        } else if (ops.includes(char)) {
            compute(num, op, stack);
            op = char;
            num = 0;
        }
    }
    compute(num, op, stack);
    return stack.reduce((prev, curr) => prev + curr, 0);
}
