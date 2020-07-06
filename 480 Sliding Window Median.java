/*
480. Sliding Window Median
https://leetcode.com/problems/sliding-window-median/

Median is the middle value in an ordered integer list.
If the size of the list is even, there is no middle value.
So the median is the mean of the two middle value.

Examples:
[2,3,4] , the median is 3
[2,3], the median is (2 + 3) / 2 = 2.5
Given an array nums, there is a sliding window of size k which is moving
from the very left of the array to the very right. You can only see the k numbers in the window.
Each time the sliding window moves right by one position.
Your job is to output the median array for each window in the original array.

For example,
Given nums = [1,3,-1,-3,5,3,6,7], and k = 3.
Window position                Median
---------------               -----
[1  3  -1] -3  5  3  6  7       1
 1 [3  -1  -3] 5  3  6  7       -1
 1  3 [-1  -3  5] 3  6  7       -1
 1  3  -1 [-3  5  3] 6  7       3
 1  3  -1  -3 [5  3  6] 7       5
 1  3  -1  -3  5 [3  6  7]      6
Therefore, return the median sliding window as [1,-1,-1,3,5,6].

Note:
You may assume k is always valid, ie: k is always smaller than input array's size for non-empty array
*/
class Solution {
    // Based on 295. Find Median from Data Stream
    // Use treeset instread of heap because data needs to be removed too.
    public double[] medianSlidingWindow(int[] nums, int k) {
        double[] result = new double[nums.length - k + 1];
        int r = 0; // iterator for result
        
        // Use 2 treesets hold the nums index, not nums value, as there can be duplicates
        // Either leftSet.size == rightSet.size or leftSet.size == rightSet.size - 1
        Comparator<Integer> comparator = (i, j) -> nums[i] != nums[j] ? Integer.compare(nums[i], nums[j]) : i - j;
        TreeSet<Integer> leftSet = new TreeSet(comparator);
        TreeSet<Integer> rightSet = new TreeSet(comparator);

        for (int i = 0; i < nums.length; ++i) {
            // Remove out of range element
            // Keep the 2 sets balanced as defined
            if (i >= k) {
                int out = i - k;
                if ((k & 1) == 0) {
                    if (!leftSet.remove(out)) {
                        rightSet.remove(out);
                        rightSet.add(leftSet.pollLast());
                    }
                } else {
                    if (!rightSet.remove(out)) {
                        leftSet.remove(out);
                        leftSet.add(rightSet.pollFirst());
                    }
                }
            }
            
            // Add new number. If same size, add to right
            // else, add to left.
            // Notice at beginning (before computing median),
            // the size comparison does not depend of k is odd or even.
            if (leftSet.size() == rightSet.size()) {
                leftSet.add(i);
                rightSet.add(leftSet.pollLast());
            } else {
                rightSet.add(i);
                leftSet.add(rightSet.pollFirst());
            }
            
            // Compute median
            if (i >= k - 1) {
                double median = ((k & 1) == 0) ? 
                    ((double)nums[leftSet.last()] + nums[rightSet.first()]) / 2.0 :
                    (double)nums[rightSet.first()] / 1.0;

                result[r] = median;
                r += 1;
            }
        }
        return result;
    }
}
