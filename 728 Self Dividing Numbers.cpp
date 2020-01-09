/*
728. Self Dividing Numbers
https://leetcode.com/problems/self-dividing-numbers/

A self-dividing number is a number that is divisible by every digit it contains.

For example, 128 is a self-dividing number because 128 % 1 == 0, 128 % 2 == 0, and 128 % 8 == 0.

Also, a self-dividing number is not allowed to contain the digit zero.

Given a lower and upper number bound, output a list of every possible self dividing number, including the bounds if possible.

Example 1:
Input: 
left = 1, right = 22
Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
Note:

The boundaries of each input argument are 1 <= left <= right <= 10000.
*/
class Solution {
public:
    bool isSelfDividing(int number) {
        if (number <= 0) {
            return false;
        }
        for (int local = number; local > 0 ; local = static_cast<int>(local / 10)) {
            int digit = local % 10;
            if (digit == 0 || number % digit != 0) {
                return false;
            }
        }
        return true;
    }
    
    std::vector<int> selfDividingNumbers(int left, int right) {
        std::vector<int> result;
        for (int i = left; i <= right; ++i) {
            if (isSelfDividing(i)) {
                result.emplace_back(i);
            }
        }  
        return result;
    }
};
