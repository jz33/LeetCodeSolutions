/*
772. Basic Calculator III
https://leetcode.com/problems/basic-calculator-iii
Consider '+', '-', '*', '/', '(', ')'
*/
type StackMember = number | string;

function compute(num: number, op: string | undefined, stack: StackMember[]) {
    // For '*', '/', compute current num with previous num.
    // For '+', '-', not compute but push the value to the stack,
    // in case there is a '*', '/' following up.
    if (op === '+') {
        stack.push(num);
    } else if (op === '-') {
        stack.push(-num);
    } else if (op === '*') {
        stack.push((stack.pop() as number) * num);
    } else if (op === '/') {
        console.log(op, stack, num);
        const r = (stack.pop() as number) / num;
        if (r > 0) {
            stack.push(Math.floor(r));
        } else {
            stack.push(Math.ceil(r));
        }
    }
}

function collapse(stack: StackMember[]) {
    // Collapse the stack to get a single number,
    // then compute with previous operator and number
    let num = 0;
    while (typeof stack[stack.length - 1] === 'number') {
        num += stack.pop() as number;
    }
    // There must be an operator ahead
    const op = stack.pop() as string;
    compute(num, op, stack);
}

function calculate(s: string) {
    let op: string | undefined = '+';

    // A stack that saves previous numbers,
    // in case of '(', it saves previous operators
    const stack: StackMember[] = [];
    // Represents current number in parsing
    let num = 0;

    for (const char of s) {
        if (['+', '-', '*', '/'].includes(char)) {
            compute(num, op, stack);
            op = char;
            num = 0;
        } else if (char === '(') {
            stack.push(op!);
            op = '+';
            num = 0;
        } else if (char === ')') {
            compute(num, op, stack);
            collapse(stack);
            op = undefined; // must be undefined, as next char should be the operator
            num = 0;
        } else {
            const digit = parseInt(char);
            if (!isNaN(digit)) {
                num = num * 10 + digit;
            }
        }
    }
    compute(num, op, stack);
    return (stack as number[]).reduce((prev, curr) => prev + curr, 0);
}
