/*
1172. Dinner Plate Stacks
https://leetcode.com/problems/dinner-plate-stacks/

You have an infinite number of stacks arranged in a row and numbered (left to right) from 0,
each of the stacks has the same maximum capacity.

Implement the DinnerPlates class:

DinnerPlates(int capacity) Initializes the object with the maximum capacity of the stacks.
void push(int val) pushes the given positive integer val into the leftmost stack with size less than capacity.

int pop() returns the value at the top of the rightmost non-empty stack and removes it from that stack,
and returns -1 if all stacks are empty.

int popAtStack(int index) returns the value at the top of the stack with the given index and removes it from that stack,
and returns -1 if the stack with that given index is empty.

Example:

Input: 
["DinnerPlates","push","push","push","push","push","popAtStack","push","push","popAtStack","popAtStack","pop","pop","pop","pop","pop"]
[[2],[1],[2],[3],[4],[5],[0],[20],[21],[0],[2],[],[],[],[],[]]

Output: 
[null,null,null,null,null,null,2,null,null,20,21,5,4,3,1,-1]

Explanation: 
DinnerPlates D = DinnerPlates(2);  // Initialize with capacity = 2
D.push(1);
D.push(2);
D.push(3);
D.push(4);
D.push(5);         // The stacks are now:  2  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 2.  The stacks are now:     4
                                                       1  3  5
                                                       ﹈ ﹈ ﹈
D.push(20);        // The stacks are now: 20  4
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.push(21);        // The stacks are now: 20  4 21
                                           1  3  5
                                           ﹈ ﹈ ﹈
D.popAtStack(0);   // Returns 20.  The stacks are now:     4 21
                                                        1  3  5
                                                        ﹈ ﹈ ﹈
D.popAtStack(2);   // Returns 21.  The stacks are now:     4
                                                        1  3  5
                                                        ﹈ ﹈ ﹈ 
D.pop()            // Returns 5.  The stacks are now:      4
                                                        1  3 
                                                        ﹈ ﹈  
D.pop()            // Returns 4.  The stacks are now:   1  3 
                                                        ﹈ ﹈   
D.pop()            // Returns 3.  The stacks are now:   1 
                                                        ﹈   
D.pop()            // Returns 1.  There are no stacks.
D.pop()            // Returns -1.  There are still no stacks.
 

Constraints:

1 <= capacity <= 20000
1 <= val <= 20000
0 <= index <= 100000
At most 200000 calls will be made to push, pop, and popAtStack.
*/
class DinnerPlates {
    private int capacity = 0;
    private int pushIndex = 0; // index of left most non-full stack
    private int popIndex = 0; // index of right most non-empty stack
    private Map<Integer, Stack<Integer>> map = new HashMap<>();
    
    public DinnerPlates(int capacity) {
        this.capacity = capacity;
    }
    
    public void push(int val) {
        // Find the left most push index
        while (map.containsKey(pushIndex) && map.get(pushIndex).size() == capacity) {
            pushIndex++;
        }
        
        // There is no "check-full" after push. This is done in next push round.
        if (!map.containsKey(pushIndex)) {
            map.put(pushIndex, new Stack<>());
        }
        map.get(pushIndex).push(val);

        // Pop index should be at least at recently pushed index.
        popIndex = Math.max(popIndex, pushIndex);
    }
    
    public int pop() {
        if (map.isEmpty()) {
            return -1;
        }

        // Find the right most pop index
        while (popIndex > -1 && map.get(popIndex).isEmpty()) {
            popIndex--;
        }

        return popAtStack(popIndex);
    }
    
    public int popAtStack(int index) {
        if (index < 0 || map.size() < index + 1 || map.get(index).isEmpty()) {
            return -1;
        }

        // Push index should be at most at recently poped index.
        pushIndex = Math.min(pushIndex, index);
        return map.get(index).pop();
    }
}
