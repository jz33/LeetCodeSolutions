/*
939. Minimum Area Rectangle
https://leetcode.com/problems/minimum-area-rectangle/

Given a set of points in the xy-plane, determine the minimum area of a rectangle formed from these points,
with sides parallel to the x and y axes.

If there isn't any rectangle, return 0.

Example 1:

Input: [[1,1],[1,3],[3,1],[3,3],[2,2]]
Output: 4

Example 2:

Input: [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
Output: 2
*/
class Solution {
public:
    int minAreaRect(vector<vector<int>>& points) {
        std::unordered_map<int, std::unordered_set<int>> book; // { x : [y]}
        for (const auto& point : points) {
            int x = point[0];
            int y = point[1];
            if (book.find(x) == book.end()) {
                std::unordered_set<int> s;
                s.insert(y);
                book[x] = s; 
            } else {
                book[x].insert(y);
            }
        }
        
        int minArea = INT_MAX;
        for (const auto& a : points) {
            for (const auto& b : points) {
                int ax = a[0];
                int ay = a[1];
                int bx = b[0];
                int by = b[1];
                if (ax != bx && ay != by) {
                    // We need 4 points, (ax, ay), (bx, by), (ax, by) and (bx, ay)
                    if (book[ax].find(by) != book[ax].end() && book[bx].find(ay) != book[bx].end()) {
                        minArea = std::min(minArea, abs((ax-bx) * (ay-by)));
                    }
                }
            }
        }
        return minArea == INT_MAX ? 0 : minArea;
    }
};
