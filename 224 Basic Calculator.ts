/*
224. Basic Calculator
https://leetcode.com/problems/basic-calculator/
Only consider '+', '-', ')', '('
Drawbacks: need to use 2 stacks ; not easily extensible to '*', '/' cases
*/ 
type Operator = '+' | '-';

function compute(num: number, op: Operator, prevNumbers: number[]) {
    if (op === '+') {
        prevNumbers.push(prevNumbers.pop()! + num);
    } else if (op === '-') {
        prevNumbers.push(prevNumbers.pop()! - num);
    }
}

function calculate(s: string): number {
    const prevNumbers: number[] = [0];
    const prevOperators: Operator[] = [];
    // Represents current number and operator in parsing
    let op: Operator = '+';
    let num = 0;
    for (const char of s) {
        if (['+', '-'].includes(char)) {
            compute(num, op, prevNumbers);
            op = char as Operator;
            num = 0;
        } else if (char === '(') {
            // Must have a 0 to compute
            prevNumbers.push(0);
            prevOperators.push(op);
            op = '+';
            num = 0;
        } else if (char === ')') {
            compute(num, op, prevNumbers);
            // Compute with previous save values
            compute(prevNumbers.pop()!, prevOperators.pop()!, prevNumbers);
            op = '+';
            num = 0;
        } else {
            const digit = parseInt(char);
            if (!isNaN(digit)) {
                num = num * 10 + digit;
            }
        }
    }
    compute(num, op, prevNumbers);
    return prevNumbers.reduce((prev, curr) => prev + curr, 0);
}

