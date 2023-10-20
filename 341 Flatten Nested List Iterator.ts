/*
341. Flatten Nested List Iterator
https://leetcode.com/problems/flatten-nested-list-iterator/

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Example 1:

Input: [[1,1],2,[1,1]]
Output: [1,1,2,1,1]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,1,2,1,1].

Example 2:

Input: [1,[4,[6]]]
Output: [1,4,6]
Explanation: By calling next repeatedly until hasNext returns false, 
             the order of elements returned by next should be: [1,4,6].

Constraints:

1 <= nestedList.length <= 500
The values of the integers in the nested list is in the range [-106, 106].
*/

/**
 * // This is the interface that allows for creating nested lists.
 * // You should not implement it, or speculate about its implementation
 * class NestedInteger {
 *     If value is provided, then it holds a single integer
 *     Otherwise it holds an empty nested list
 *     constructor(value?: number) {
 *         ...
 *     };
 *
 *     Return true if this NestedInteger holds a single integer, rather than a nested list.
 *     isInteger(): boolean {
 *         ...
 *     };
 *
 *     Return the single integer that this NestedInteger holds, if it holds a single integer
 *     Return null if this NestedInteger holds a nested list
 *     getInteger(): number | null {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a single integer equal to value.
 *     setInteger(value: number) {
 *         ...
 *     };
 *
 *     Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
 *     add(elem: NestedInteger) {
 *         ...
 *     };
 *
 *     Return the nested list that this NestedInteger holds,
 *     or an empty list if this NestedInteger holds a single integer
 *     getList(): NestedInteger[] {
 *         ...
 *     };
 * };
 */

class NestedIterator {
  // The index points to next NestedIterator object 
  private index: number = 0;
  // The stack saves the last state
  private stack: {list: NestedInteger[], index: number}[] = [];
  // The list is the last iterated object
  private list: NestedInteger[] = [];

  constructor(nestedList: NestedInteger[]) {
    this.list = nestedList;
  }

  hasNext(): boolean {
    while (this.index < this.list.length || this.stack.length > 0) {
      if (this.index < this.list.length) {
        const element = this.list[this.index];
        if (element.isInteger()) {
          // Has the value
          return true;
        } else {
          // Save the last state to stack and move into nested list
          this.stack.push({
            list: this.list,
            index: this.index + 1,
          });
          this.list = element.getList();
          this.index = 0;
        }
      }
      else {
        const pair = this.stack.pop();
        this.list = pair!.list;
        this.index  = pair!.index;
      }
    }
    return false;
  }

  next(): number {
    const value = this.list[this.index].getInteger();
    this.index += 1;
    return value;
  }
}

/**
 * Your ParkingSystem object will be instantiated and called as such:
 * var obj = new NestedIterator(nestedList)
 * var a: number[] = []
 * while (obj.hasNext()) a.push(obj.next());
 */
