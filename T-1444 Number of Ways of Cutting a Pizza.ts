/*
1444. Number of Ways of Cutting a Pizza
https://leetcode.com/problems/number-of-ways-of-cutting-a-pizza/

Given a rectangular pizza represented as a rows x cols matrix containing the following characters:
'A' (an apple) and '.' (empty cell) and given the integer k. You have to cut the pizza into k pieces using k-1 cuts. 

For each cut you choose the direction: vertical or horizontal, then you choose a cut position at the cell boundary and
cut the pizza into two pieces. If you cut the pizza vertically, give the left part of the pizza to a person.
If you cut the pizza horizontally, give the upper part of the pizza to a person. Give the last piece of pizza to the last person.

Return the number of ways of cutting the pizza such that each piece contains at least one apple. Since the answer can be a huge number,
return this modulo 10^9 + 7.

Example 1:

Input: pizza = ["A..","AAA","..."], k = 3
Output: 3 
Explanation: The figure above shows the three ways to cut the pizza. Note that pieces must contain at least one apple.

Example 2:

Input: pizza = ["A..","AA.","..."], k = 3
Output: 1

Example 3:

Input: pizza = ["A..","A..","..."], k = 1
Output: 1

Constraints:

1 <= rows, cols <= 50
rows == pizza.length
cols == pizza[i].length
1 <= k <= 10
pizza consists of characters 'A' and '.' only.
*/
class PrefixSumMatrix {
    prefix: number[][] = []
    rowCount: number
    colCount: number

    constructor(matrix: string[]) {
        this.rowCount = matrix.length;
        this.colCount = matrix[0].length;

        let prefix: number[][] = []
        for (let i = 0; i < this.rowCount + 1; ++i) {
            prefix[i] = []
            for (let j = 0; j < this.colCount + 1; ++j) {
                prefix[i][j] = 0
            }
        }

        for (let i = 0; i < this.rowCount; ++i) {
            for (let j = 0; j < this.colCount; ++j) {
                prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j]
                if (matrix[i][j] === 'A') {
                    prefix[i+1][j+1]  += 1
                }
            }
        }

        this.prefix = prefix
    }

    /**
     * Get sum from top left (i0, j0) till bottom right (i1, j1), both inclusive
     */
    getSum(i0: number, j0:number, i1?: number, j1?:number): number {
        const prefix = this.prefix
        if (!i1) {
            i1 = this.rowCount - 1
        }
        if (!j1) {
            j1 = this.colCount - 1
        }
        return prefix[i1+1][j1+1] - prefix[i0][j1+1] - prefix[i1+1][j0] + prefix[i0][j0]
    }
}

/**
 * A simple map with a numeric array as the key.
 * Because javascript cannot use array as Map's key!
 */
class Cache {
    map: Map<string, any> = new Map()

    has(key: any[]): boolean {
        return this.map.has(key.toString())
    }

    set(key: any[], val: any): void {
        this.map.set(key.toString(), val)
    }

    get(key: any[]): any {
        return this.map.get(key.toString())
    }
}

function ways(pizza: string[], k: number): number {
    const rowCount: number = pizza.length;
    const colCount: number = pizza[0].length;
    
    const pp = new PrefixSumMatrix(pizza)
    const mod = 10 ** 9 + 7
    let cache = new Cache()

    /**
     * Recursive top down dynamic programming call
     * @param r: row index of top-left point
     * @param c: column index of top-left point
     * @param d: how many cut already done
     */
    function topDown(r: number, c: number, d: number): number{
        const key: number[] = [r, c, d]
        if (cache.has(key)) {
            return cache.get(key)!
        }

        let res: number = 0
        if (pp.getSum(r, c) === 0) {
            res = 0
        }
        else if (d === k - 1) {
            res = 1
        }
        else {
            // Cut horizontally
            for (let i = r + 1; i < rowCount; ++i) {
                if (pp.getSum(r, c) - pp.getSum(i, c) > 0) {
                    res = (res + topDown(i, c, d + 1)) % mod
                }
            }

            // Cut vertically  
            for (let j = c + 1; j < colCount; ++j) {
                if (pp.getSum(r, c) - pp.getSum(r, j) > 0) {
                    res = (res + topDown(r, j, d + 1)) % mod
                }
            }
        }

        cache.set(key, res)
        return res
    }

    return topDown(0, 0, 0)
}
