/*
605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n,
return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true

Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

Constraints:
    1 <= flowerbed.length <= 2 * 104
    flowerbed[i] is 0 or 1.
    There are no two adjacent flowers in flowerbed.
    0 <= n <= flowerbed.length
*/
function canPlaceFlowers(flowerbed: number[], n: number): boolean {
    let filledSlots = 0;
    // Record whether previous slot is filled, considering original and newly filled flowers
    let previousSlotFilled = false;
    for (let i = 0; i < flowerbed.length && filledSlots < n; i++) {
        const slot = flowerbed[i];
        if (slot === 1) {
            previousSlotFilled = true;
        } else if (previousSlotFilled) {
            previousSlotFilled = false;
        } else if (i === flowerbed.length - 1 || flowerbed[i + 1] !== 1) {
            // Only when previous slot is not filled, current slot is not filled,
            // and next slot is not filled, can fill current slot.
            previousSlotFilled = true;
            filledSlots++;
        }
    }
    return filledSlots === n;
};
