/*
218. The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/
*/
class Solution {
public:
    vector<vector<int>> getSkyline(vector<vector<int>>& buildings) {
        std::vector<std::pair<int,int>> src; // [position, height]
        
        for (auto& b : buildings) {
            src.emplace_back(b[0], b[2]);
            src.emplace_back(b[1], -b[2]); // Set minus if leaving building
        }

        // Notice the sort order is not by default.
        // If 2 pairs has same position, bigger height goes front,
        // because we want new building enter before old building leave.
        std::sort(src.begin(), src.end(), [](const auto& a, const auto& b) -> bool {
            if (a.first == b.first) {
                return a.second > b.second;
            } else {
                return a.first < b.first;
            }
        });
        
        int prevHeight = 0;
        std::map<int, int> heightMap; // {height : count}
        heightMap[0] = 1; // For the first rbegin() call
        std::vector<std::vector<int>> skyline;
            
        for (auto& b : src) {
            int position = b.first;
            int height = b.second;
            
            if (height > 0) {
                heightMap[height]++;
            } else {
                height = -height;
                int ctr = heightMap[height];
                if (ctr == 1) {
                    heightMap.erase(height);
                } else {
                    heightMap[height]--;
                }
            }
            
            int maxHeight = heightMap.rbegin()->first;
            if (maxHeight != prevHeight) {
                prevHeight = maxHeight;
                std::vector<int> pair {position, maxHeight};
                skyline.emplace_back(pair);
            }
        }
             
        return skyline;    
    }
};
