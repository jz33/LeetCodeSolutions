/*
218. The Skyline Problem
https://leetcode.com/problems/the-skyline-problem/
*/
class Solution {
public:
    std::vector<std::vector<int>> getSkyline(std::vector<std::vector<int>>& buildings) {
        std::vector<std::pair<int, int>> heights; // [[location, height]]
        for (auto& b : buildings) {
            heights.emplace_back(b[0], -b[2]);
            heights.emplace_back(b[1], b[2]);
        }
        
        // Sort by location then height. Since building entry's height is minus,
        // then building entry point will be removed from TreeMap first.
        std::stable_sort(heights.begin(), heights.end(), [](const auto& a, const auto& b) -> bool {
            if (a.first == b.first) {
                return a.second < b.second;
            } else {
                return a.first < b.first;
            }
        });
        
        // TreeMap, stores {height : count}
        std::map<int, int> heightMap;
        heightMap.emplace(0, 1);
        
        int prevHeight = 0;
        std::vector<std::vector<int>> skyLine;
        
        for (auto& pair : heights) {
            int h = pair.second;
            if (h < 0) {
                // Put height for new building
                heightMap[-h]++;
            } else {
                // Reduce or remove height
                int ctr = heightMap[h];
                if (ctr == 1) {
                    heightMap.erase(h);
                } else {
                    heightMap[h]--;
                }
            }
            
            int maxHeight = heightMap.rbegin()->first;
            if (maxHeight != prevHeight) {
                std::vector<int> pp {pair.first, maxHeight};
                skyLine.emplace_back(pp);
                prevHeight = maxHeight;
            }
        }
        return skyLine;
    }
};
